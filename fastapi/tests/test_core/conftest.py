import pytest
from testcontainers.core.waiting_utils import wait_for_logs
from testcontainers.core import utils
from fastapi.testclient import TestClient
from database.postgres import Base
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session
from testcontainers.postgres import PostgresContainer
from main import app


POSTGRES_IMAGE = "postgres:15"
POSTGRES_USER = "postgres"
POSTGRES_PASSWORD = "test_password"
POSTGRES_DATABASE = "test_database"
POSTGRES_CONTAINER_PORT = 5432


class BaseTestSettings:
    @pytest.fixture(scope="session")
    def postgres_container(self) -> PostgresContainer:
        postgres = PostgresContainer(
            image=POSTGRES_IMAGE,
            user=POSTGRES_USER,
            password=POSTGRES_PASSWORD,
            dbname=POSTGRES_DATABASE,
            port=POSTGRES_CONTAINER_PORT,
        )
        with postgres:
            wait_for_logs(
                postgres,
                r"UTC \[1\] LOG:  database system is ready to accept connections",
                10,
            )
            yield postgres

    @pytest.fixture(autouse=True)
    def truncate_tables(self, db_session: Session):
        with db_session as connection:
            for table in Base.metadata.tables:
                stm = text(f'TRUNCATE TABLE "{table}" RESTART IDENTITY CASCADE')
                connection.execute(statement=stm)

    @pytest.fixture(scope="session")
    def db(self, postgres_container: PostgresContainer):
        if utils.is_windows():
            postgres_container.get_container_host_ip = lambda: "localhost"
        url = postgres_container.get_connection_url()
        engine = create_engine(url, echo=False, future=True)
        Base.metadata.create_all(engine)
        with Session(engine) as session:
            yield session

    @pytest.fixture(scope="session")
    def test_client(self, db):
        app.dependency_overrides[db_session] = lambda: db
        with TestClient(app) as c:
            yield c
        app.dependency_overrides.clear()

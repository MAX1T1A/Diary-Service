from fastapi.testclient import TestClient
from testcontainers.core.utils import is_windows
from database.postgres import Base, get_db
from database.postgres import sessionmaker
from sqlalchemy import create_engine
from testcontainers.postgres import PostgresContainer
from core.config import settings
from testcontainers.core.waiting_utils import wait_for_logs
import pytest
from main import app


class BaseTestSettings:
    @pytest.fixture(scope="session")
    def postgres_container(self) -> PostgresContainer:
        postgres = PostgresContainer(
            user=settings.postgres.user,
            password=settings.postgres.password,
            dbname=settings.test_postgres.dbname,
            port=settings.postgres.port,
            image="postgres:15"
        )
        with postgres:
            wait_for_logs(
                postgres,
                r"UTC \[1\] LOG:  database system is ready to accept connections", 10)
            yield postgres

    @pytest.fixture(scope="session")
    def db(self, postgres_container: PostgresContainer) -> sessionmaker:
        if is_windows():
            postgres_container.get_container_host_ip = lambda: settings.test_postgres.host
        url = postgres_container.get_connection_url()
        engine = create_engine(url, pool_size=20, max_overflow=0)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        with Session() as session:
            yield session

    @pytest.fixture(scope="session")
    def test_client(self, db) -> TestClient:
        app.dependency_overrides[get_db] = lambda: db
        client: TestClient = TestClient(app)
        try:
            yield client
        finally:
            app.dependency_overrides.clear()

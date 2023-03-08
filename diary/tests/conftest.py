import pytest
from fastapi import FastAPI
from testcontainers.core.waiting_utils import wait_for_logs
from database.postgres import Base
from core.config import settings
from sqlalchemy import create_engine, text, Engine
from testcontainers.postgres import PostgresContainer
from main import build_app
from fastapi.testclient import TestClient


@pytest.fixture(scope="session")
def postgres_container() -> PostgresContainer:
    postgres = PostgresContainer(
        image="postgres:latest", user=settings.postgres.user, password=settings.postgres.password, dbname=settings.postgres.dbname, port=settings.postgres.port)
    with postgres:
        wait_for_logs(postgres, r"UTC \[1\] LOG:  database system is ready to accept connections", 10)
        yield postgres


@pytest.fixture(scope="session")
def provide_engine_singleton(postgres_container: PostgresContainer) -> Engine:
    engine = create_engine(postgres_container.get_connection_url(), echo=False, future=True)
    Base.metadata.create_all(engine)
    yield engine


@pytest.fixture(scope="function", autouse=True)
def truncate_tables(provide_engine_singleton) -> None:
    with provide_engine_singleton.begin() as connection:
        for table in ("user", "diary", "page"):
            stm = text(f'TRUNCATE TABLE "{table}" RESTART IDENTITY CASCADE')
            connection.execute(statement=stm)
    connection.commit()


@pytest.fixture(scope="session")
def provide_app(provide_engine_singleton) -> FastAPI:
    return build_app(provide_engine_singleton)


@pytest.fixture(scope="session")
def client(provide_app) -> TestClient:
    with TestClient(provide_app) as client:
        yield client

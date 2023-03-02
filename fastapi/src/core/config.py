import os
from pydantic import BaseSettings

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENV_DIR = os.path.join(BASE_DIR, "..", "..")


class JWTSettings(BaseSettings):
    secret_key: str
    algorithm: str
    active_time: int


class PostgresSettings(BaseSettings):
    host: str
    port: int
    dbname: str
    user: str
    password: str


class TestPostgresSettings(BaseSettings):
    dbname: str
    host: str


class Settings(BaseSettings):
    test_postgres: TestPostgresSettings
    postgres: PostgresSettings
    jwt_token: JWTSettings

    class Config:
        #  Для локальной разработки вне docker
        env_file = (
            os.path.join(ENV_DIR, ".env"),
            os.path.join(ENV_DIR, ".env.dev"),
        )
        env_nested_delimiter = "__"


settings = Settings()

import os

from pydantic import BaseSettings

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENV_DIR = os.path.join(BASE_DIR, "..", "..")


class PostgresSettings(BaseSettings):
    host: str
    port: int
    dbname: str
    user: str
    password: str


class Settings(BaseSettings):
    postgres: PostgresSettings


settings = Settings()

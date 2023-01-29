import os

from pydantic import BaseSettings, BaseModel


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENV_DIR = os.path.join(BASE_DIR, "..", "..")


class PostgresSettings(BaseSettings):
    host: str
    port: int
    dbname: str
    user: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class Settings(BaseSettings):
    postgres: PostgresSettings
    token: Token

    class Config:
        #  Для локальной разработки вне docker
        env_file = (
            os.path.join(ENV_DIR, ".env.prod"),
            os.path.join(ENV_DIR, ".env.dev"),
        )
        env_nested_delimiter = "__"


settings = Settings()

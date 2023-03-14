import logging
import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from core.config import settings

db_uri = (
    "postgresql+psycopg2://"
    f"{settings.postgres.user}:{settings.postgres.password}@"
    f"{settings.postgres.host}:{settings.postgres.port}/"
    f"{settings.postgres.dbname}"
)
engine = create_engine(db_uri, pool_size=20, max_overflow=0)
Session = sessionmaker(bind=engine, autocommit=False, autoflush=False)
db_session = scoped_session(Session)

Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    from models.models import User, Diary, Page


def get_db():
    database = Session()
    try:
        yield database
    finally:
        database.close()

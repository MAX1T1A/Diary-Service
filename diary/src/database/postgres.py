from core.config import settings
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

db_uri = (
    "postgresql+psycopg2://"
    f"{settings.postgres.user}:{settings.postgres.password}@"
    f"{settings.postgres.host}:{settings.postgres.port}/"
    f"{settings.postgres.dbname}"
)

Base = declarative_base()


def init_db():
    from models.models import Diary, Page, User

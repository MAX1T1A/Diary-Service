import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from dotenv import load_dotenv

load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'postgres:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

engine = create_engine(f'postgresql+psycopg2://{os.getenv("POSTGRES__USER")}:{os.getenv("POSTGRES__PASSWORD")}'
                       f'@{os.getenv("POSTGRES__HOST")}:{os.getenv("POSTGRES__PORT")}/{os.getenv("POSTGRES__DBNAME")}',
                       pool_pre_ping=True)
engine.connect()

db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

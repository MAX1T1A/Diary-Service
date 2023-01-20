import sqlalchemy
from sqlalchemy import create_engine, MetaData, ForeignKey
from databases import Database
from core.config import WTN_DATABASE_URL

database = Database(WTN_DATABASE_URL)
metadata = MetaData()
engine = create_engine(
    WTN_DATABASE_URL,
)


user_table = sqlalchemy.Table(
    "user",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True),
    sqlalchemy.Column("email", sqlalchemy.String, primary_key=True, unique=True),
    sqlalchemy.Column("name", sqlalchemy.String, nullable=False),
    sqlalchemy.Column("password", sqlalchemy.String, nullable=False),
)


diary_table = sqlalchemy.Table(
    "diary",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True),
    sqlalchemy.Column("name", sqlalchemy.String),
)


page_table = sqlalchemy.Table(
    "page",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True),
    sqlalchemy.Column("name", sqlalchemy.String),
    sqlalchemy.Column("body", sqlalchemy.Text),
)


user_diary_table = sqlalchemy.Table(
    "user_diary",
    metadata,
    sqlalchemy.Column("user_id", sqlalchemy.Integer, ForeignKey("user.id")),
    sqlalchemy.Column("diary_id", sqlalchemy.Integer, ForeignKey("diary.id")),
)


diary_page_table = sqlalchemy.Table(
    "diary_page",
    metadata,
    sqlalchemy.Column("diary_id", sqlalchemy.Integer, ForeignKey("diary.id")),
    sqlalchemy.Column("page_id", sqlalchemy.Integer, ForeignKey("page.id")),
)

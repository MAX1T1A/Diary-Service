import sqlalchemy
from users import users_table

from models import metadata


diaries_table = sqlalchemy.Table(
    "diaries",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True),
    sqlalchemy.Column("user_id", sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id")),
    sqlalchemy.Column("name", sqlalchemy.String),
)

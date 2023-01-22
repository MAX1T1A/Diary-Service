import sqlalchemy
from diaries import diaries_table

from models import metadata


pages_table = sqlalchemy.Table(
    "pages",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True),
    sqlalchemy.Column("diary_id", sqlalchemy.Integer, sqlalchemy.ForeignKey("diaries.id")),
    sqlalchemy.Column("name", sqlalchemy.String),
    sqlalchemy.Column("body", sqlalchemy.Text),
)

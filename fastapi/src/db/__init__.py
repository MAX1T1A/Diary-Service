from models.user import User

from db.postgres import metadata, engine

metadata.create_all(bind=engine)

from starlette.config import Config
from dotenv import load_dotenv
import os

load_dotenv()

config = Config(".env")

DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("BD_PASS")
DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")


WTN_DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

ACCESS_TOKEN_EXPIRE_MINUTES = 60
ALGORITHM = "HS256"
SECRET_KEY = config("EE_SECRET_KEY", cast=str, default="2b2d197649061838c0c381612cb117d5f562ff181f2ed68c7847471af22f83ce")

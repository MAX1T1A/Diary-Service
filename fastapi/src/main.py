from fastapi import FastAPI
from api.v1 import user_routes, diary_routes, page_routes
from sqlalchemy.engine import Engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.orm import Session

app = FastAPI(title="Diary API")


def build_app(engine: Engine):
    app.include_router(user_routes.router, prefix="/api/v1", tags=["Auth"])
    app.include_router(diary_routes.router, prefix="/api/v1", tags=["Diary"])
    app.include_router(page_routes.router, prefix="/api/v1", tags=["Diary Pages"])

    return app


def setup_di(engine: Engine, app: FastAPI):
    session = sessionmaker(engine)
    s


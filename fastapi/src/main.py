from fastapi import FastAPI
from api.v1 import user_routes, diary_routes, page_routes
from sqlalchemy.engine import Engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.orm import Session
from services.providers import stub_user_service, get_user_service

app = FastAPI(title="Diary API")


def build_app(engine: Engine):
    app.include_router(user_routes.router, prefix="/api/v1", tags=["Auth"])
    # app.include_router(diary_routes.router, prefix="/api/v1", tags=["Diary"])
    # app.include_router(page_routes.router, prefix="/api/v1", tags=["Diary Pages"])

    return app


def setup_di(engine: Engine, app: FastAPI):
    session = sessionmaker(engine)

    user_service = lambda: get_user_service(session)
    app.dependency_overrides[stub_user_service] = user_service

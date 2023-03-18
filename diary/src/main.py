from api.v1 import diary_routes, page_routes, user_routes
from database.postgres import db_uri
from fastapi import FastAPI
from services.providers import *
from sqlalchemy.engine import Engine, create_engine

application = FastAPI(title="Diary API")


def build_app(eng: Engine):
    setup(eng=eng, app=application)
    application.include_router(user_routes.router, prefix="/api/v1", tags=["Auth"]),
    application.include_router(diary_routes.router, prefix="/api/v1", tags=["Diary"]),
    application.include_router(
        page_routes.router, prefix="/api/v1", tags=["Diary Pages"]
    )
    return application


def setup(eng: Engine, app: FastAPI):
    Session = sessionmaker(bind=eng)
    with Session() as session:
        app.dependency_overrides[stub_user_service] = lambda: get_user_service(
            session=session
        )
        app.dependency_overrides[stub_diary_service] = lambda: get_diary_service(
            session=session
        )
        app.dependency_overrides[stub_page_service] = lambda: get_page_service(
            session=session
        )


def get_app():
    engine = create_engine(db_uri, pool_size=20, max_overflow=0)

    return build_app(eng=engine)

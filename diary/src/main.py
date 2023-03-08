from fastapi import FastAPI
from api.v1 import user_routes, diary_routes, page_routes
from sqlalchemy.engine import Engine
from services.providers import *

application = FastAPI(title="Diary API")


def build_app(engine: Engine):
    setup(engine=engine, app=application)
    application.include_router(user_routes.router, prefix="/api/v1", tags=["Auth"])
    application.include_router(diary_routes.router, prefix="/api/v1", tags=["Diary"])
    application.include_router(page_routes.router, prefix="/api/v1", tags=["Diary Pages"])

    return application


def setup(engine: Engine, app: FastAPI):
    Session = sessionmaker(bind=engine)
    with Session() as session:
        app.dependency_overrides[stub_user_service] = lambda: get_user_service(session=session)
        app.dependency_overrides[stub_diary_service] = lambda: get_diary_service(session=session)
        app.dependency_overrides[stub_page_service] = lambda: get_page_service(session=session)

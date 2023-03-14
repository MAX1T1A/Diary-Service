import uvicorn
from fastapi import FastAPI
from api.v1 import user_routes, diary_routes, page_routes
from sqlalchemy.engine import Engine
from services.providers import *

application = FastAPI(title="Diary API")


def routers():
    return application.include_router(user_routes.router, prefix="/api/v1", tags=["Auth"]), \
        application.include_router(diary_routes.router, prefix="/api/v1", tags=["Diary"]),\
        application.include_router(page_routes.router, prefix="/api/v1", tags=["Diary Pages"])


def build_app(engine: Engine):
    setup(engine=engine, app=application)
    routers()
    return application


def setup(engine: Engine, app: FastAPI):
    Session = sessionmaker(bind=engine)
    with Session() as session:
        app.dependency_overrides[stub_user_service] = lambda: get_user_service(session=session)
        app.dependency_overrides[stub_diary_service] = lambda: get_diary_service(session=session)
        app.dependency_overrides[stub_page_service] = lambda: get_page_service(session=session)


routers()

if __name__ == "__main__":
    uvicorn.run("main:application", host="0.0.0.0", port=8000)

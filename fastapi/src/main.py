import uvicorn
from fastapi import FastAPI
from api.v1 import user_routes, diary_routes, page_routes

app = FastAPI(title="Diary API")

app.include_router(user_routes.router, prefix="/api/v1", tags=["Auth"])
app.include_router(diary_routes.router, prefix="/api/v1", tags=["Diary"])
app.include_router(page_routes.router, prefix="/api/v1", tags=["Diary Pages"])

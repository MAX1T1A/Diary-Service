from fastapi import FastAPI
import uvicorn

from api.v1 import user_routes, diary_routes

app = FastAPI(title="Diary API")

app.include_router(user_routes.router, prefix="/api/v1", tags=["Auth"])
app.include_router(diary_routes.router, prefix="/api/v1", tags=["Diary"])

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, host="127.0.0.1", reload=True)

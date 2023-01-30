from fastapi import FastAPI
from api.v1 import user_routes
import uvicorn

app = FastAPI(title="Diary API")
app.include_router(user_routes.router)


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, host="127.0.0.1", reload=True)

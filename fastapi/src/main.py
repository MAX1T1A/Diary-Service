from fastapi import FastAPI
import uvicorn

app = FastAPI(title="Employment exchange")


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, host="127.0.0.1", reload=True)

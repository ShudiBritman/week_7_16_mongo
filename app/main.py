from fastapi import FastAPI
from contextlib import asynccontextmanager
import uvicorn
from routes import router
from db import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()

app = FastAPI(lifespan=lifespan)
    
app.include_router(
    router
)

@app.get("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
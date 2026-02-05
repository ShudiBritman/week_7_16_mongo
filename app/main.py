from fastapi import FastAPI
import uvicorn
from db import init_db
from routes import router


app = FastAPI()
    
@app.on_event("startup")
async def lifespan():
    init_db()



@app.get("/health")
async def health():
    return {"status": "ok"}

app.include_router(
        router
)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
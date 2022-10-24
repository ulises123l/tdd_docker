# project/app/main.py
  
from fastapi import FastAPI, Depends

from app.config import get_settings, Settings

app = FastAPI()

@app.get("/ping")
async def pong(settigns: Settings = Depends(get_settings)):
    return {
        "ping": "pong!",
        "environment": settigns.environment,
        "testing": settigns.testing
    }
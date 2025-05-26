from fastapi import FastAPI, WebSocket
from .database import engine, Base
from . import models, chat

app = FastAPI()

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.websocket("/ws/{username}")
async def websocket_endpoint(websocket: WebSocket, username: str):
    await websocket.accept()
    await chat.chat_sender(websocket, username)

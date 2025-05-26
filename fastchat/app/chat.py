import aioredis
from fastapi import WebSocket

REDIS_URL = "redis://redis:6379"

async def chat_listener(websocket: WebSocket, username: str):
    redis = await aioredis.from_url(REDIS_URL)
    pubsub = redis.pubsub()
    await pubsub.subscribe("chat")

    try:
        async for message in pubsub.listen():
            if message["type"] == "message":
                await websocket.send_text(message["data"].decode())
    except Exception as e:
        await websocket.close()
    finally:
        await pubsub.unsubscribe("chat")

async def chat_sender(websocket: WebSocket, username: str):
    redis = await aioredis.from_url(REDIS_URL)
    try:
        while True:
            data = await websocket.receive_text()
            await redis.publish("chat", f"{username}: {data}")
    except Exception:
        await websocket.close()

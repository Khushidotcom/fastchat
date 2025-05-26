# FastChat - Real-Time Chat App with FastAPI, WebSockets & Redis

## Features
- Real-time messaging via WebSockets
- Redis Pub/Sub for scalable message handling
- PostgreSQL for user/message storage
- JWT-based authentication
- Dockerized setup

## Setup
```bash
docker-compose up --build
```

Then go to: `http://localhost:8000`

## WebSocket Example
Connect to: `ws://localhost:8000/ws/<username>`

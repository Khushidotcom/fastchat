# 🗨️ FastChat – Real-Time Scalable Chat App with FastAPI

A production-ready, real-time messaging app built using **FastAPI**, **WebSockets**, **Redis Pub/Sub**, **PostgreSQL**, and **Docker**.

## 🚀 Features

- 🔐 JWT-based user authentication
- 💬 Real-time messaging using WebSockets
- 📡 Scalable Pub/Sub message broadcasting via Redis
- 🗃️ PostgreSQL to store messages and users
- 🐳 Fully Dockerized for easy deployment
- 🔧 Clean and modular backend structure (ready for microservices)

## 🛠️ Tech Stack

- **Backend**: Python, FastAPI, WebSockets
- **Database**: PostgreSQL
- **Cache/Broker**: Redis Pub/Sub
- **Auth**: JWT (HS256)
- **DevOps**: Docker, Docker Compose
- **ORM**: SQLAlchemy (Async)

## 📦 Setup Instructions

> Make sure Docker is installed on your system

```bash
git clone https://github.com/Khushidotcom/fastchat.git
cd fastchat
docker-compose up --build

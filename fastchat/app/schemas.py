from pydantic import BaseModel
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    id: int
    username: str

class Token(BaseModel):
    access_token: str
    token_type: str

class Message(BaseModel):
    sender_id: int
    content: str
    timestamp: datetime

from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str
    email: str
    password: str


class RoomCreate(BaseModel):
    name: str


class MessageCreate(BaseModel):
    content: str
    room_id: int
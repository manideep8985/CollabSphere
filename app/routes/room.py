from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from jose import jwt, JWTError
from app.database import SessionLocal
from app import models, schemas

router = APIRouter()

SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"


def get_db():
    db = SessionLocal()
    yield db


def get_current_user(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload["user_id"]
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")


@router.post("/create")
def create_room(
    room: schemas.RoomCreate,
    token: str,
    db: Session = Depends(get_db)
):
    user_id = get_current_user(token)

    new_room = models.Room(
        name=room.name,
        owner_id=user_id
    )

    db.add(new_room)
    db.commit()
    db.refresh(new_room)

    return new_room
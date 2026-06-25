from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import models

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/add")
def add_task(text: str, room_id: int, db: Session = Depends(get_db)):
    task = models.Task(
        text=text,
        status="todo",
        room_id=room_id
    )

    db.add(task)
    db.commit()
    db.refresh(task)

    return task


@router.get("/{room_id}")
def get_tasks(room_id: int, db: Session = Depends(get_db)):
    return db.query(models.Task).filter(models.Task.room_id == room_id).all()


@router.put("/{task_id}")
def update_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()

    if task.status == "todo":
        task.status = "progress"
    elif task.status == "progress":
        task.status = "done"
    else:
        task.status = "todo"

    db.commit()
    return task

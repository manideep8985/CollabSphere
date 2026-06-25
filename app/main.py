from fastapi import FastAPI
from app.database import engine
from app import models
from app.routes import user, room, chat
from app.routes import task

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="CollabSphere 🚀")

app.include_router(user.router, prefix="/users", tags=["Users"])
app.include_router(room.router, prefix="/rooms", tags=["Rooms"])
app.include_router(chat.router)
app.include_router(task.router, prefix="/tasks", tags=["Tasks"])
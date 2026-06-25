from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from app.database import SessionLocal
from app import models

router = APIRouter()

connections = {}


@router.websocket("/ws/{room_id}/{user_id}")
async def websocket_endpoint(websocket: WebSocket, room_id: int, user_id: int):

    await websocket.accept()
    print("✅ Connected:", user_id)

    if room_id not in connections:
        connections[room_id] = []

    connections[room_id].append(websocket)

    db = SessionLocal()

    # ✅ Send old messages when user connects
    old_messages = db.query(models.Message).filter(
        models.Message.room_id == room_id
    ).all()

    for msg in old_messages:
        await websocket.send_text(f"User {msg.user_id}: {msg.content}")

    try:
        while True:
            data = await websocket.receive_text()

            print("Message:", data)

            # ✅ Save to DB
            new_msg = models.Message(
                content=data,
                room_id=room_id,
                user_id=user_id
            )

            db.add(new_msg)
            db.commit()

            # ✅ Broadcast
            for conn in connections[room_id]:
                await conn.send_text(f"User {user_id}: {data}")

    except WebSocketDisconnect:
        print("❌ Disconnected:", user_id)
        connections[room_id].remove(websocket)
        db.close()
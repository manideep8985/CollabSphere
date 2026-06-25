<h1 align="center">🚀 CollabSphere</h1>
<p align="center">
Real-time collaborative platform combining chat, task management, and room-based workflows.
</p>

---

## 🧠 Overview

CollabSphere is a full-stack collaboration platform designed to enable real-time communication and productivity within shared rooms.

It integrates:
- ⚡ Real-time messaging using WebSockets  
- 📌 Task management workflows  
- 🏠 Room-based collaboration  
- 🔐 Authentication system  

This project demonstrates backend scalability, real-time architecture, and modern UI design.

---

## ✨ Key Features

### 💬 Real-Time Communication
- WebSocket-based bi-directional communication
- Multi-user chat with instant updates
- Room-based message isolation

### ✅ Task Workflow Management
- Kanban-style board (Todo → In Progress → Done)
- Click-based task state transitions
- Backend persistence using REST APIs

### 🏠 Room System
- Dynamic room creation
- Independent workspace per room
- Shared collaboration spaces

### 🔐 Authentication System
- User registration and login APIs
- Token-based authentication (JWT ready)

### 🎨 UI/UX Design
- Modern dark-theme interface
- Clean minimal layout inspired by Slack/Notion
- Responsive and user-friendly

---

## 🏗 System Architecture

      ┌───────────────┐
            │   Frontend    │
            │ HTML/CSS/JS   │
            └──────┬────────┘
                   │ REST + WebSocket
            ┌──────▼────────┐
            │   FastAPI     │
            │   Backend     │
            └──────┬────────┘
                   │
            ┌──────▼────────┐
            │   Database    │
            │   (SQLite)    │
            └───────────────┘


---

## 🛠 Tech Stack

### Backend
- FastAPI
- SQLAlchemy ORM
- WebSockets
- SQLite

### Frontend
- HTML
- CSS (custom UI)
- JavaScript (vanilla)

---

## ⚙️ Installation & Setup

```bash
# Clone repository
git clone https://github.com/manideep8985/CollabSphere.git
cd CollabSphere

# Install dependencies
pip install -r requirements.txt

# Run backend
uvicorn app.main:app --reload

Open the frontend:
index.html


🌐 API Endpoints
Authentication
POST /users/register
POST /users/login

Tasks
GET    /tasks/{room_id}
POST   /tasks/add
PUT    /tasks/{task_id}

WebSocket
ws://localhost:8000/ws/{room_id}/{user_id}


📸 Screenshots
💬 Chat Interface
./screenshots/chat.png
✅ Task Board
./screenshots/tasks.png

🚀 Future Enhancements

🔄 Drag & Drop Task Management
🤖 AI-powered chat summarization
📁 File sharing & attachments
🔔 Notification system
🌍 Cloud deployment & scaling


📊 Engineering Highlights

Designed asynchronous WebSocket handling using FastAPI
Implemented REST + real-time hybrid architecture
Structured modular backend (routes, models, services)
Built state-driven frontend without frameworks
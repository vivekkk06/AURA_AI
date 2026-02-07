# 🧠 AURA AI – Multi User AI Platform

AURA AI is a full-stack AI-powered multi-user platform built using:

- ⚡ FastAPI (Backend)
- 🎨 Streamlit (Frontend)
- 🧠 Groq LLaMA 3.1 (LLM)
- 🗄 MongoDB
- 🎥 YouTube Data API
- 🎙 Faster-Whisper
- 📧 Email Notification System

---

# 🚀 Live Project Structure

```
AURA_AI/
│
├── backend/
│   ├── main.py
│   ├── core/
│   ├── db/
│   ├── modules/
│   │   ├── youtube_ai/
│   │   ├── chat_ai/
│   │   ├── document_ai/
│   │   ├── news_research/
│   │   └── memory/
│   └── requirements.txt
│
├── frontend/
│   ├── app.py
│   ├── pages/
│   │   ├── youtube_ai.py
│   │   ├── chat_ai.py
│   │   ├── document_qa.py
│   │   ├── memory_dashboard.py
│   │   └── news_research.py
│
└── README.md
```

---

# ✨ Core Features

## 🔐 Authentication System
- JWT-based login/signup
- Multi-user session management
- Secure token validation
- Per-user data isolation

---

## 💬 Chat AI
- Conversational AI powered by Groq (LLaMA 3.1)
- User memory storage
- Persistent conversation tracking

---

## 🎥 YouTube AI

### 🔹 Instant Quick Summary
- High-level summary generated immediately

### 🔹 Background Full Summary
- Detailed structured summary
- Runs asynchronously
- Auto-refresh updates UI

### 🔹 Metadata Fetching
Displays:
- 🎬 Title
- 📺 Channel
- 🖼 Thumbnail
- 👁 Views
- 👍 Likes
- 👥 Subscribers
- ⏱ Duration

### 🔹 Transcript Toggle
Switch between:
- AI Summary
- Raw Transcript

### 🔹 PDF Download
Download summary as PDF.

### 🔹 Audio Upload Fallback
If captions unavailable:
- User uploads audio
- Whisper transcribes
- AI generates summary

---

## 📄 Document AI
- Upload document
- Ask contextual questions
- AI-generated answers

---

## 🧠 Memory Dashboard
- View stored user interactions
- Clean UI memory panel
- Per-user database separation

---

## 📰 News Research AI
- AI-assisted research system
- Context-aware news analysis

---

## 📧 Email Sending System

AURA AI includes an integrated email notification system.

### Features:
- Sends verification emails
- Sends alerts or system messages
- SMTP-based email delivery
- Secure credentials via environment variables

### Environment Variables Required:

```
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USER=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
```

> ⚠ For Gmail:
Enable App Passwords and use that instead of your normal password.

---

# 🏗 Tech Stack

## Backend
- FastAPI
- MongoDB
- Groq LLM API
- YouTube Data API v3
- Faster-Whisper
- yt-dlp
- JWT Authentication
- SMTP Email Service

## Frontend
- Streamlit
- Custom CSS Glass UI
- ReportLab (PDF generation)

---

# ⚙️ Installation Guide

---

## 1️⃣ Clone Repository

```bash
git clone https://github.com/vivekkk06/AURA_AI.git
cd AURA_AI
```

---

## 2️⃣ Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## 3️⃣ Create `.env` File (Inside backend)

```
GROQ_API_KEY=your_groq_key
YOUTUBE_API_KEY=your_youtube_key
MONGO_URL=mongodb://localhost:27017
SECRET_KEY=your_secret_key

EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USER=your_email
EMAIL_PASSWORD=your_app_password
```

---

## 4️⃣ Run Backend

```bash
uvicorn main:app --reload
```

Backend runs at:
```
http://127.0.0.1:8000
```

---

## 5️⃣ Frontend Setup

Open new terminal:

```bash
cd frontend
python -m venv .venv
source .venv/bin/activate
pip install streamlit requests reportlab
```

Run frontend:

```bash
streamlit run app.py
```

App runs at:
```
http://localhost:8501
```

---

# 🛠 Required External Tools

## Install yt-dlp

```bash
pip install yt-dlp
```

## Install FFmpeg

Linux:
```bash
sudo dnf install ffmpeg
```

---

# 🔁 Background Processing Flow

YouTube AI works as:

1. User pastes URL
2. Quick summary generated instantly
3. MongoDB stores stage
4. Background task generates full summary
5. Frontend auto-refresh fetches updated result

---

# 🔐 Security

- JWT Authentication
- Token validation middleware
- Protected API routes
- MongoDB ObjectId handling
- Secure environment variables

---

# 💡 Architecture Highlights

- Clean modular backend structure
- Separate service, routes, and transcript layers
- No blocking LLM calls
- Async background task handling
- Multi-user session-safe system

---

# 🧑‍💻 Author

**Vivek Badgujar**

GitHub:
https://github.com/vivekkk06/AURA_AI

---

# 📌 Future Improvements

- Docker support
- Cloud deployment
- Role-based access control
- Analytics dashboard
- UI animations upgrade

---

# 📜 License

This project is built for educational and portfolio purposes.

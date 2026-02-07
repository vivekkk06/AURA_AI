# 🧠 MULTI USER AI PLATFORM

An advanced multi-user AI platform built with **FastAPI + Streamlit + MongoDB + Groq LLM**.

This project includes:

- 💬 Chat AI
- 🎥 YouTube AI (Quick + Full Summary with Metadata)
- 📄 Document AI
- 🧠 Memory Dashboard
- 📰 News Research
- 🔐 Authentication System
- 👥 Multi-user session handling

---

# 🚀 Features

## 🎥 YouTube AI
- Quick summary (instant)
- Full detailed summary (background processing)
- Auto-refresh status
- View:
  - Title
  - Channel
  - Thumbnail
  - Views
  - Likes
  - Subscribers
  - Duration
- Transcript toggle
- Download summary as PDF
- Audio upload fallback (Whisper AI)

---

## 💬 Chat AI
- Conversational AI powered by Groq
- User-based memory
- Session isolation

---

## 📄 Document AI
- Upload document
- Ask questions
- Context-based answers

---

## 🧠 Memory Dashboard
- View stored conversation history
- Per-user data separation

---

## 📰 News Research
- AI powered research assistant

---

# 🏗 Tech Stack

## Backend
- FastAPI
- MongoDB
- Groq (LLaMA 3.1)
- Faster-Whisper
- YouTube Data API

## Frontend
- Streamlit
- Custom CSS UI
- ReportLab (PDF generation)

---

# 📂 Project Structure

```
multi_user_AI/
│
├── backend/
│   ├── main.py
│   ├── modules/
│   │   ├── youtube_ai/
│   │   ├── chat_ai/
│   │   ├── document_ai/
│   │   ├── memory/
│   │   └── news_research/
│   ├── db/
│   ├── core/
│   └── requirements.txt
│
├── frontend/
│   ├── app.py
│   ├── pages/
│   │   ├── chat_ai.py
│   │   ├── youtube_ai.py
│   │   ├── document_qa.py
│   │   ├── memory_dashboard.py
│   │   └── news_research.py
│
└── README.md
```

---

# ⚙️ Installation Guide

## 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd multi_user_AI
```

---

## 2️⃣ Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows

pip install -r requirements.txt
```

---

## 3️⃣ Environment Variables

Create `.env` inside backend folder:

```
GROQ_API_KEY=your_groq_api_key
YOUTUBE_API_KEY=your_youtube_api_key
MONGO_URL=mongodb://localhost:27017
SECRET_KEY=your_secret_key
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

# 🎥 YouTube AI Flow

1. User pastes YouTube URL
2. Quick summary generated instantly
3. Full summary runs in background
4. Auto-refresh updates result
5. User can:
   - Toggle transcript
   - Download PDF
   - View metadata

If captions unavailable:
- User can upload audio file
- Whisper transcribes
- AI generates summary

---

# 🛠 Required External Tools

Install:

### yt-dlp
```bash
pip install yt-dlp
```

### FFmpeg
Linux:
```bash
sudo dnf install ffmpeg
```

---

# 🔐 Authentication

- JWT-based authentication
- Multi-user session isolation
- MongoDB-based storage

---

# 📦 API Endpoints

## YouTube AI

```
POST /youtube/summarize
GET  /youtube/status
POST /youtube/upload-audio
```

---

# 🧠 Background Processing

FastAPI BackgroundTasks:
- Quick summary → immediate
- Full summary → async background
- MongoDB stage tracking

---

# 📥 PDF Export

Summary can be downloaded as PDF using ReportLab.

---

# ⚠️ Important Notes

- Do NOT commit:
  - .env
  - venv
  - audio files
- Add proper `.gitignore`

---

# 🧑‍💻 Author

Vivek Badgujar

Built using:
FastAPI + Streamlit + Groq + MongoDB

---

# 📜 License

This project is for educational & personal use.

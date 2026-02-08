<<<<<<< HEAD
🧠 AURA AI – Multi User AI Platform
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

✨ Core Features
🔐 Authentication System

Email OTP verification

JWT-based login

Multi-user session management

Secure token validation

Per-user data isolation

Password hashing using Argon2

💬 Chat AI

Groq-powered conversational AI (LLaMA 3.1)

Persistent user memory

MongoDB conversation storage

Multi-session safe architecture

🎥 YouTube AI
⚡ Instant Quick Summary

High-level summary generated immediately

🧠 Background Full Summary

Detailed structured summary

Runs asynchronously

Auto-refresh UI updates

📊 Metadata Display

🎬 Title

📺 Channel

🖼 Thumbnail

👁 Views

👍 Likes

👥 Subscribers

⏱ Duration

📜 Transcript Toggle

Switch between:

AI Summary

Raw Transcript

📥 PDF Export

Download summary as PDF (ReportLab)

🎙 Audio Upload Fallback

If captions unavailable:

User uploads audio

Whisper transcribes

AI generates summary

📄 Document AI

Upload PDF

Ask contextual questions

Vector search (FAISS)

Sentence-transformers embeddings

🧠 Memory Dashboard

View stored user interactions

Clean UI memory panel

Per-user database separation

📰 News Research AI

AI-assisted news analysis

Web scraping (BeautifulSoup)

Context-aware summarization

📧 Email Notification System

OTP verification emails

SMTP-based delivery

Secure credentials via environment variables

Gmail App Password supported

🏗 Tech Stack
Backend

FastAPI

MongoDB

Groq API

YouTube Data API v3

Faster-Whisper

yt-dlp

JWT Authentication

SMTP Email Service

Frontend

Streamlit

Custom Glass UI CSS

ReportLab (PDF export)

⚙️ Installation Guide
1️⃣ Clone Repository
git clone https://github.com/vivekkk06/AURA_AI.git
cd AURA_AI

2️⃣ Backend Setup
Create Virtual Environment
🐧 Linux / macOS
cd backend
python3 -m venv venv
source venv/bin/activate

🪟 Windows
cd backend
python -m venv venv
venv\Scripts\activate

Install Dependencies
pip install -r requirements.txt

3️⃣ Create .env File (Inside backend folder)

Create a file named .env and add:

GROQ_API_KEY=your_groq_key
YOUTUBE_API_KEY=your_youtube_api_key
MONGO_URL=mongodb://localhost:27017
SECRET_KEY=your_secret_key

EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USER=your_email@gmail.com
EMAIL_PASSWORD=your_gmail_app_password


⚠ Important:

Do NOT use your real Gmail password.

Enable App Passwords in Google account security.

Use that generated password.

Your project securely reads these using os.getenv().

4️⃣ Run Backend
uvicorn main:app --reload


Backend runs at:

http://127.0.0.1:8000

5️⃣ Frontend Setup

Open new terminal.

🐧 Linux / macOS
cd frontend
python3 -m venv .venv
source .venv/bin/activate

🪟 Windows
cd frontend
python -m venv .venv
.venv\Scripts\activate

Install Dependencies
pip install streamlit requests reportlab

Run Frontend
streamlit run app.py


Frontend runs at:

http://localhost:8501

🛠 Required External Tools
Install yt-dlp
pip install yt-dlp

Install FFmpeg
Linux (Fedora)
sudo dnf install ffmpeg

Ubuntu
sudo apt install ffmpeg

macOS
brew install ffmpeg

Windows

Download from:
https://ffmpeg.org/download.html

Add to system PATH.

🔁 Background Processing Flow
=======
# 🧠 AURA AI -- Multi User AI Platform

AURA AI is a full-stack AI-powered multi-user platform built with modern
AI infrastructure and a clean modular architecture.

------------------------------------------------------------------------

## 🚀 Tech Stack

### Backend

-   ⚡ FastAPI
-   🗄 MongoDB
-   🧠 Groq (LLaMA 3.1)
-   🎥 YouTube Data API v3
-   🎙 Faster-Whisper
-   🔐 JWT Authentication
-   📧 SMTP Email System

### Frontend

-   🎨 Streamlit
-   📄 ReportLab (PDF Export)
-   ✨ Custom Glass UI

------------------------------------------------------------------------

## ✨ Core Features

### 🔐 Authentication

-   Email OTP verification
-   Argon2 password hashing
-   JWT login
-   Secure protected routes
-   Multi-user session isolation

### 🎥 YouTube AI

-   Instant quick summary
-   Background detailed summary
-   Metadata display (Views, Likes, Subs, Duration)
-   Transcript toggle
-   PDF download
-   Audio upload fallback (Whisper transcription)

### 💬 Chat AI

-   Groq-powered LLaMA 3.1 chat
-   Persistent memory storage
-   Per-user conversation history

### 📄 Document AI

-   Upload PDFs
-   Ask contextual questions
-   Vector search (FAISS)

### 📰 News Research AI

-   Web scraping
-   AI summarization
-   Context-aware research

### 🧠 Memory Dashboard

-   View stored interactions
-   Clean per-user data separation

------------------------------------------------------------------------

## 📁 Project Structure

AURA_AI/ │ ├── backend/ │ ├── main.py │ ├── core/ │ ├── db/ │ ├──
modules/ │ └── requirements.txt │ ├── frontend/ │ ├── app.py │ ├──
pages/ │ └── components/ │ └── README.md

------------------------------------------------------------------------

## ⚙️ Installation Guide

### 1️⃣ Clone Repository

git clone https://github.com/vivekkk06/AURA_AI.git cd AURA_AI

------------------------------------------------------------------------

### 2️⃣ Backend Setup

Linux/macOS: python3 -m venv venv source venv/bin/activate

Windows: python -m venv venv venv`\Scripts`{=tex}`\activate`{=tex}

Install dependencies: pip install -r requirements.txt

------------------------------------------------------------------------

### 3️⃣ Environment Variables (.env inside backend)

GROQ_API_KEY=your_groq_key YOUTUBE_API_KEY=your_youtube_key
MONGO_URL=mongodb://localhost:27017 SECRET_KEY=your_secret_key

EMAIL_HOST=smtp.gmail.com EMAIL_PORT=587 EMAIL_USER=your_email@gmail.com
EMAIL_PASSWORD=your_app_password

⚠ Use Gmail App Password, not your real password.

------------------------------------------------------------------------

### 4️⃣ Run Backend

uvicorn main:app --reload

Backend URL: http://127.0.0.1:8000

------------------------------------------------------------------------

### 5️⃣ Frontend Setup

cd frontend python -m venv .venv source .venv/bin/activate (Linux/macOS)
.venv`\Scripts`{=tex}`\activate  `{=tex}(Windows)

pip install streamlit requests reportlab

Run: streamlit run app.py

Frontend URL: http://localhost:8501

------------------------------------------------------------------------

## 🛠 Required External Tools

Install yt-dlp: pip install yt-dlp

Install FFmpeg:

Linux: sudo dnf install ffmpeg

Ubuntu: sudo apt install ffmpeg

macOS: brew install ffmpeg

Windows: Download from https://ffmpeg.org/download.html and add to PATH.

------------------------------------------------------------------------
>>>>>>> 48c05b0 (Final readme.md)

## 🔐 Security

<<<<<<< HEAD
User pastes URL

Quick summary generated instantly

MongoDB stores stage

Background task generates full summary

Frontend auto-refresh fetches updated result

Non-blocking architecture.

🔐 Security

JWT Authentication

Token validation middleware

MongoDB ObjectId handling

Argon2 password hashing

Environment variable secret storage

No credentials stored in repository

🧑‍💻 Author

Vivek Badgujar

GitHub:
https://github.com/vivekkk06/AURA_AI

📌 Future Improvements

Docker containerization

Cloud deployment (AWS / GCP / Azure)

Role-based access control

Analytics dashboard

UI animation upgrades

CI/CD integration

📜 License

This project is built for educational and portfolio purposes.
=======
-   JWT authentication
-   Environment-based secrets
-   No credentials stored in repository
-   MongoDB ObjectId protection
-   Secure password hashing

------------------------------------------------------------------------

## 👨‍💻 Author

Vivek Badgujar\
GitHub: https://github.com/vivekkk06/AURA_AI

------------------------------------------------------------------------

## 📜 License

Built for educational and portfolio purposes.
>>>>>>> 48c05b0 (Final readme.md)

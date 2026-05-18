# AURA AI -- Multi User AI Platform

AURA AI is a full-stack AI-powered multi-user platform built with modern
AI infrastructure and a clean modular architecture.

------------------------------------------------------------------------

## Tech Stack

### Backend

-   FastAPI
-   MongoDB
-   Groq (LLaMA 3.1)
-   YouTube Data API v3
-   Faster-Whisper
-   JWT Authentication
-   SMTP Email System

### Frontend

-   Streamlit
-   ReportLab (PDF Export)
-   Custom Glass UI

------------------------------------------------------------------------

## Core Features

###  Authentication

-   Email OTP verification
-   Argon2 password hashing
-   JWT login
-   Secure protected routes
-   Multi-user session isolation

###  YouTube AI

-   Instant quick summary
-   Background detailed summary
-   Metadata display (Views, Likes, Subs, Duration)
-   Transcript toggle
-   PDF download
-   Audio upload fallback (Whisper transcription)

###  Chat AI

-   Groq-powered LLaMA 3.1 chat
-   Persistent memory storage
-   Per-user conversation history

###  Document AI

-   Upload PDFs
-   Ask contextual questions
-   Vector search (FAISS)

###  News Research AI

-   Web scraping
-   AI summarization
-   Context-aware research

###  Memory Dashboard

-   View stored interactions
-   Clean per-user data separation

------------------------------------------------------------------------

##  Project Structure

AURA_AI/ │ ├── backend/ │ ├── main.py │ ├── core/ │ ├── db/ │ ├──
modules/ │ └── requirements.txt │ ├── frontend/ │ ├── app.py │ ├──
pages/ │ └── components/ │ └── README.md

------------------------------------------------------------------------

##  Installation Guide

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

##  Required External Tools

Install yt-dlp: pip install yt-dlp

Install FFmpeg:

Linux: sudo dnf install ffmpeg

Ubuntu: sudo apt install ffmpeg

macOS: brew install ffmpeg

Windows: Download from https://ffmpeg.org/download.html and add to PATH.

------------------------------------------------------------------------

##  Security

-   JWT authentication
-   Environment-based secrets
-   No credentials stored in repository
-   MongoDB ObjectId protection
-   Secure password hashing

------------------------------------------------------------------------

##  Author

Vivek Badgujar\
GitHub: https://github.com/vivekkk06/AURA_AI

------------------------------------------------------------------------

## 📜 License

Built for educational and portfolio purposes.

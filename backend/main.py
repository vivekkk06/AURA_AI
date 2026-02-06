from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db.mongo import client

from auth.routes import router as auth_router
from modules.chat.routes import router as chat_router
from modules.resume_ai.routes import router as resume_router
from modules.dashboard.routes import router as dashboard_router
from modules.memory.routes import router as memory_router
from modules.documents.routes import router as docs_router
from modules.multi_agent.routes import router as agent_router
from modules.news_agent.routes import router as news_router
from modules.youtube_ai.routes import router as youtube_router

app = FastAPI(title="MULTI USER AI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup():
    client.admin.command("ping")
    print("✅ MongoDB connected")

app.include_router(auth_router)
app.include_router(chat_router)
app.include_router(resume_router)
app.include_router(dashboard_router)
app.include_router(memory_router)
app.include_router(docs_router)
app.include_router(agent_router)
app.include_router(news_router)
app.include_router(youtube_router)

@app.get("/health")
def health():
    return {"status": "healthy"}

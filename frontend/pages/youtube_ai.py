import streamlit as st
import time
from components.api import api_post_json, api_get
from components.ui import load_css

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="YouTube AI | MULTI USER AI",
    page_icon="🎥",
    layout="wide",
    initial_sidebar_state="expanded"
)

load_css()

# ------------------ AUTH ------------------
if "token" not in st.session_state:
    st.error("🔐 Please login first")
    st.stop()

# ---------------- USER CHANGE RESET ----------------
if "last_user" not in st.session_state:
    st.session_state.last_user = st.session_state.current_user

if st.session_state.last_user != st.session_state.current_user:
    # clear only youtube page state
    for k in ["yt_summary", "yt_url", "processing", "stage", "last_check"]:
        if k in st.session_state:
            del st.session_state[k]

    st.session_state.last_user = st.session_state.current_user


# ------------------ SIDEBAR ------------------
with st.sidebar:
    st.markdown("<h2 style='text-align:center;'>🧠 MULTI USER AI</h2>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)

    st.success("✅ Logged in")
    if st.button("🚪 Logout", use_container_width=True):
        st.session_state.clear()
        st.rerun()

    st.markdown("### 📂 Navigation")

    st.page_link("app.py", label="🏠 Home")
    st.page_link("pages/chat_ai.py", label="💬 Chat AI")
    st.page_link("pages/resume_ai.py", label="📄 Resume AI")
    st.page_link("pages/memory_dashboard.py", label="🧠 Memory Dashboard")
    st.page_link("pages/document_qa.py", label="📄 Document AI")
    st.page_link("pages/news_research.py", label="📰 News Research")
    # st.page_link("pages/youtube_ai.py", label="🎥 YouTube AI")
    st.page_link("pages/About.py", label="ℹ About")
    st.caption("⚡ Powered by FastAPI + LangChain + Groq")
    st.caption("made by Vivek Badgujar")

# ------------------ HERO ------------------
st.markdown("""
<div style="text-align:center; padding:30px 0;">
    <h1>🎥 YouTube AI</h1>
    <h4>Quick summary first • Full summary in background</h4>
</div>
""", unsafe_allow_html=True)

# ------------------ CARD STYLE ------------------
st.markdown("""
<style>
.yt-card {
    background: radial-gradient(circle at top left, #0f172a, #020617);
    padding: 30px;
    border-radius: 22px;
    border: 1px solid rgba(148,163,184,0.15);
    box-shadow: 0 0 35px rgba(56,189,248,0.08);
    max-width: 900px;
    margin: auto;
}
</style>
""", unsafe_allow_html=True)

# ------------------ MAIN CARD ------------------
# st.markdown("<div class='yt-card'>", unsafe_allow_html=True)

st.markdown("## ▶ YouTube Video Summarizer")
st.caption("⚡ Quick summary → 🧠 Full summary → 🔄 Auto-updating")

url = st.text_input("📎 Paste YouTube video URL")

# ------------------ GENERATE ------------------
if st.button("🧠 Generate Summary", use_container_width=True):
    r = api_post_json("/youtube/summarize", {"url": url})
    data = r.json()

    st.session_state.yt_url = url
    st.session_state.yt_summary = data.get("summary")
    st.session_state.stage = data.get("stage")
    st.session_state.processing = True
    st.session_state.last_check = time.time()

# ------------------ AUTO REFRESH ------------------
if st.session_state.get("processing"):
    if time.time() - st.session_state.get("last_check", 0) > 8:
        r = api_get(f"/youtube/status?url={st.session_state.yt_url}")
        data = r.json()

        st.session_state.yt_summary = data.get("summary")
        st.session_state.stage = data.get("stage")
        st.session_state.last_check = time.time()

        if data.get("status") == "done":
            st.session_state.processing = False

# ------------------ STAGE DISPLAY ------------------
stage_map = {
    "transcribing": "🔊 Transcribing audio…",
    "quick_summary": "⚡ Creating quick summary…",
    "full_summary": "🧠 Generating full summary…",
    "completed": "✅ Completed",
    "error": "❌ Error occurred"
}

if st.session_state.get("stage"):
    st.info(stage_map.get(st.session_state.stage, "⏳ Processing…"))

# ------------------ RESULT ------------------
if "yt_summary" in st.session_state:
    st.divider()
    st.subheader("📄 Video Summary")
    st.markdown(st.session_state.yt_summary)

st.markdown("</div>", unsafe_allow_html=True)

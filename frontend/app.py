import streamlit as st
from components.ui import load_css

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="MULTI USER AI",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

load_css()

# ------------------ SIDEBAR ------------------
with st.sidebar:
    st.markdown("<h2 style='text-align:center;'>🧠 MULTI USER AI</h2>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)

    if "token" not in st.session_state:
        st.info("🔐 You are not logged in")
        st.page_link("pages/login.py", label="🔑 Login")
        st.page_link("pages/register.py", label="📝 Register")
    else:
        st.success("✅ Logged in")
        if st.button("🚪 Logout", use_container_width=True):
            st.session_state.clear()
            st.rerun()

    # st.markdown("<br>")
    st.markdown("### 📂 Navigation")

    # st.page_link("pages/1_app.py", label="🏠 Home")
    st.page_link("pages/chat_ai.py", label="💬 Chat AI")
    st.page_link("pages/resume_ai.py", label="📄 Resume AI")
    st.page_link("pages/memory_dashboard.py", label="🧠 Memory Dashboard")
    st.page_link("pages/document_qa.py", label="📄 Document AI")
    st.page_link("pages/news_research.py", label="📰 News Research")
    st.page_link("pages/youtube_ai.py", label="🎥 YouTube AI")
    # st.markdown("<br><hr>")
    st.caption("⚡ Powered by FastAPI + LangChain + Groq")
    st.caption("made by Vivek Badgujar")

# ------------------ HERO ------------------
st.markdown("""
<div style="text-align:center; padding:35px 0;">
    <h1>🚀 MULTI USER AI</h1>
    <h4>Your all-in-one Multi-Agent AI Platform</h4>
</div>
""", unsafe_allow_html=True)

# ------------------ UI STYLES ------------------
st.markdown("""
<style>
.feature-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 22px;
}

.feature-card {
    background: radial-gradient(circle at top, #0f172a, #020617);
    border: 1px solid rgba(148,163,184,0.12);
    border-radius: 22px;
    padding: 22px;
    height: 300px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    transition: all 0.35s ease;
    box-shadow: 0 0 15px rgba(79,70,229,0.15);
}

.feature-card:hover {
    transform: translateY(-6px) scale(1.02);
    box-shadow:
        0 0 25px rgba(99,102,241,0.6),
        0 0 60px rgba(139,92,246,0.4);
    border: 1px solid rgba(99,102,241,0.6);
}

.feature-title {
    font-size: 22px;
    font-weight: 700;
}

.feature-text {
    color: #cbd5e1;
    font-size: 14px;
    margin-top: 6px;
    line-height: 1.5;
}

div.stButton > button {
    width: 100%;
    height: 44px;
    border-radius: 14px;
    background: linear-gradient(90deg,#4f46e5,#7c3aed);
    color: white;
    font-weight: 600;
    border: none;
    transition: all 0.25s ease;
}

div.stButton > button:hover {
    background: linear-gradient(90deg,#6366f1,#8b5cf6);
    box-shadow: 0 0 15px rgba(139,92,246,0.8);
    transform: scale(1.03);
}
</style>
""", unsafe_allow_html=True)

# ------------------ FEATURE GRID ------------------
st.markdown('<div class="feature-grid">', unsafe_allow_html=True)

# ---- CHAT AI ----
with st.container():
    st.markdown("""
    <div class="feature-card">
        <div>
            <div class="feature-title">💬 Chat AI</div>
            <div class="feature-text">
                Talk with intelligent multi-agent AI system.
            </div>
        </div>
    """, unsafe_allow_html=True)

    if st.button("Open Chat AI", key="chat"):
        st.switch_page("pages/chat_ai.py")

    st.markdown("</div>", unsafe_allow_html=True)

# ---- RESUME AI ----
with st.container():
    st.markdown("""
    <div class="feature-card">
        <div>
            <div class="feature-title">📄 Resume AI</div>
            <div class="feature-text">
                AI-powered interview & resume evaluator.
            </div>
        </div>
    """, unsafe_allow_html=True)

    if st.button("Open Resume AI", key="resume"):
        st.switch_page("pages/Resume_AI.py")

    st.markdown("</div>", unsafe_allow_html=True)

# ---- MEMORY ----
with st.container():
    st.markdown("""
    <div class="feature-card">
        <div>
            <div class="feature-title">🧠 Memory System</div>
            <div class="feature-text">
                Persistent user-based AI memory & recall system.
            </div>
        </div>
    """, unsafe_allow_html=True)

    if st.button("Open Memory Dashboard", key="memory"):
        st.switch_page("pages/Memory_Dashboard.py")

    st.markdown("</div>", unsafe_allow_html=True)

# ---- DASHBOARD ----
with st.container():
    st.markdown("""
    <div class="feature-card">
        <div>
            <div class="feature-title"> 📹 YouTube Video to summary</div>
            <div class="feature-text">
                Complete summary and insights from YouTube videos.
            </div>
        </div>
    """, unsafe_allow_html=True)

    if st.button("Open Youtube-summary-translator", key="dash"):
        st.switch_page("pages/Youtube_AI.py")

    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.info("👉 Use the sidebar to explore all AI systems.")

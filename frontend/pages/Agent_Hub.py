import streamlit as st
from components.ui import load_css

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Agent Hub | MULTI USER AI",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

load_css()

# ------------------ AUTH ------------------
if "token" not in st.session_state:
    st.error("🔐 Please login first")
    st.stop()

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
    st.page_link("pages/youtube_ai.py", label="🎥 YouTube AI")
    st.page_link("pages/About.py", label="ℹ About")
    
    st.caption("⚡ Powered by FastAPI + LangChain + Groq")
    st.caption("made by Vivek Badgujar")

# ------------------ HERO ------------------
st.markdown("""
<div style="text-align:center; padding:30px 0;">
    <h1>🧠 Agent Hub</h1>
    <h4>Central control panel of your AI ecosystem</h4>
</div>
""", unsafe_allow_html=True)

# ------------------ STYLE ------------------
st.markdown("""
<style>
.glass {
    background: radial-gradient(circle at top left, #0f172a, #020617);
    border-radius: 22px;
    padding: 25px;
    border: 1px solid rgba(148,163,184,0.15);
    box-shadow: 0 0 35px rgba(56,189,248,0.08);
    margin-bottom: 25px;
    transition: 0.3s;
}
.glass:hover {
    box-shadow: 0 0 45px rgba(56,189,248,0.25);
    transform: translateY(-5px);
}
.soft {
    color: #94a3b8;
}
</style>
""", unsafe_allow_html=True)

# ================= GRID =================
r1c1, r1c2, r1c3 = st.columns(3)
r2c1, r2c2, r2c3 = st.columns(3)

with r1c1:
    with st.container(border=True):
        st.markdown("### 💬 Chat AI")
        st.markdown("<p class='soft'>Multi-agent intelligent conversation system</p>", unsafe_allow_html=True)
        if st.button("Open Chat AI", use_container_width=True):
            st.switch_page("pages/chat_ai.py")

with r1c2:
    with st.container(border=True):
        st.markdown("### 📄 Resume AI")
        st.markdown("<p class='soft'>Resume intelligence & interview engine</p>", unsafe_allow_html=True)
        if st.button("Open Resume AI", use_container_width=True):
            st.switch_page("pages/resume_ai.py")

with r1c3:
    with st.container(border=True):
        st.markdown("### 📚 Document AI")
        st.markdown("<p class='soft'>Chat with PDFs and documents</p>", unsafe_allow_html=True)
        if st.button("Open Document AI", use_container_width=True):
            st.switch_page("pages/document_qa.py")

with r2c1:
    with st.container(border=True):
        st.markdown("### 🧩 News Research AI")
        st.markdown("<p class='soft'>Multi-agent news research system</p>", unsafe_allow_html=True)
        if st.button("Open News Research", use_container_width=True):
            st.switch_page("pages/news_research.py")

with r2c2:
    with st.container(border=True):
        st.markdown("### 📊 Memory Dashboard")
        st.markdown("<p class='soft'>AI memory, logs & analytics</p>", unsafe_allow_html=True)
        if st.button("Open Memory Dashboard", use_container_width=True):
            st.switch_page("pages/memory_dashboard.py")

with r2c3:
    with st.container(border=True):
        st.markdown("### 🎥 YouTube Intelligence")
        st.markdown("<p class='soft'>AI-powered video understanding</p>", unsafe_allow_html=True)
        if st.button("Open YouTube AI", use_container_width=True):
            st.switch_page("pages/youtube_ai.py")

# ---------------- FOOTER ----------------
st.divider()
st.success("⚡ Agent Hub is the central control panel of your AI ecosystem.")

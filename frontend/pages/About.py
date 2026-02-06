import streamlit as st
from components.ui import load_css

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="About | AURA AI",
    page_icon="ℹ",
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
    

    st.caption("⚡ Powered by FastAPI + LangChain + Groq")
    st.caption("made by Vivek Badgujar")

# ------------------ HERO ------------------
st.markdown("""
<div style="text-align:center; padding:30px 0 15px 0;">
    <h1>ℹ About AURA AI</h1>
    <p style="color:#94a3b8; font-size:17px;">
        A full-stack, multi-agent, industry-grade Generative AI engineering platform
    </p>
</div>
""", unsafe_allow_html=True)

# ------------------ STYLE ------------------
st.markdown("""
<style>
.glass {
    background: radial-gradient(circle at top left, #0f172a, #020617);
    border-radius: 22px;
    padding: 28px;
    border: 1px solid rgba(148,163,184,0.15);
    box-shadow: 0 0 35px rgba(56,189,248,0.08);
    margin-bottom: 26px;
}
.section-title {
    font-size: 28px;
    font-weight: 800;
}
.soft {
    color: #94a3b8;
    font-size: 16px;
    line-height: 1.65;
}
</style>
""", unsafe_allow_html=True)

# ------------------ ABOUT ------------------
st.markdown("""
<div class="glass">
    <div class="section-title">🧠 What is AURA AI?</div>
    <p class="soft">
        <b>AURA AI</b> is a production-style <b>multi-user Generative AI platform</b> engineered to demonstrate 
        real-world AI system design — not just chatbots.
        <br><br>
        It unifies <b>LLMs, agents, tools, vector search, document intelligence, resume analysis, news research,
        and YouTube understanding</b> into one intelligent ecosystem.
        <br><br>
        This platform is designed as a <b>resume-grade, internship-level, and startup-style AI engineering project</b>.
    </p>
</div>
""", unsafe_allow_html=True)

# ---------------- STACK + SYSTEMS ----------------
c1, c2 = st.columns(2)

with c1:
    st.markdown("""
    <div class="glass">
        <div class="section-title">⚙ Core Technology Stack</div>
        <p class="soft">
        • FastAPI microservice backend<br>
        • Streamlit professional frontend<br>
        • LangChain pipelines & tools<br>
        • LangGraph multi-agent workflows<br>
        • Groq Cloud inference (LLMs)<br>
        • MongoDB user & memory store<br>
        • Vector databases for RAG<br>
        • Secure JWT authentication
        </p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="glass">
        <div class="section-title">🧩 AI Systems Inside AURA</div>
        <p class="soft">
        • Multi-Agent Chat AI<br>
        • Resume Intelligence Engine<br>
        • AI Interview Generator<br>
        • Document Question Answering (RAG)<br>
        • AI News Researcher System<br>
        • YouTube Video Understanding & Summarization<br>
        • Memory Dashboard & recall system
        </p>
    </div>
    """, unsafe_allow_html=True)

# ---------------- ARCHITECTURE ----------------
st.markdown("""
<div class="glass">
    <div class="section-title">🏗 Platform Architecture</div>
    <p class="soft">
    ✔ Secure multi-user authentication layer<br>
    ✔ Modular AI service architecture<br>
    ✔ Independent AI agent pipelines<br>
    ✔ Retrieval-augmented generation (RAG)<br>
    ✔ Role-aware intelligence systems<br>
    ✔ AI + tools hybrid reasoning models<br>
    ✔ Scalable backend and clean API design
    </p>
</div>
""", unsafe_allow_html=True)

# ---------------- PURPOSE ----------------
st.markdown("""
<div class="glass">
    <div class="section-title">🎯 Vision & Purpose</div>
    <p class="soft">
    AURA AI was built to demonstrate:
    <br><br>
    ✔ Real-world AI engineering workflows<br>
    ✔ End-to-end GenAI product design<br>
    ✔ Multi-agent system architecture<br>
    ✔ LLM + data + tools integration<br>
    ✔ Industry-level project depth
    <br><br>
    This platform can be presented as:
    <br>
    • Internship shortlisting project<br>
    • Advanced academic AI project<br>
    • Startup MVP foundation<br>
    • Professional AI portfolio system
    </p>
</div>
""", unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.divider()
st.success("AURA AI is a professional-grade AI engineering platform demonstrating modern GenAI system design.")

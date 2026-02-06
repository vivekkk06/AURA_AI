import streamlit as st
from components.api import api_post_json
from components.ui import load_css

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="AI News Researcher | MULTI USER AI",
    page_icon="📰",
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
    # st.markdown("<hr>", unsafe_allow_html=True)

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
    # st.page_link("pages/news_research.py", label="📰 News Research")
    st.page_link("pages/youtube_ai.py", label="🎥 YouTube AI")
    st.page_link("pages/About.py", label="ℹ About")
    st.caption("⚡ Powered by FastAPI + LangChain + Groq")
    st.caption("made by Vivek Badgujar")

# ------------------ HERO ------------------
st.markdown("""
<div style="text-align:center; padding:30px 0;">
    <h1>📰 AI News Researcher</h1>
    <h4>Multi-agent system to research, analyze, and summarize live news topics</h4>
</div>
""", unsafe_allow_html=True)

# ------------------ CARD STYLE ------------------
st.markdown("""
<style>
.news-card {
    background: radial-gradient(circle at top left, #0f172a, #020617);
    padding: 30px;
    border-radius: 22px;
    border: 1px solid rgba(148,163,184,0.15);
    box-shadow: 0 0 35px rgba(56,189,248,0.08);
    max-width: 1200px;
    margin: auto;
}
</style>
""", unsafe_allow_html=True)

# ------------------ MAIN CARD ------------------
# st.markdown("<div class='news-card'>", unsafe_allow_html=True)

# ---------------- INPUT ----------------
st.subheader("🔎 Start New Research")

c1, c2 = st.columns([4, 1])

with c1:
    topic = st.text_input(
        "Research topic",
        placeholder="Artificial Intelligence in healthcare, ISRO missions, OpenAI, stock market trends..."
    )

with c2:
    search_btn = st.button("🚀 Research", use_container_width=True)

# ---------------- PROCESS ----------------
if topic and search_btn:
    with st.spinner("🧠 AI agents are scanning, analyzing, and summarizing the news..."):
        r = api_post_json("/agent/news", {"topic": topic})

        if r.status_code == 200:
            report = r.json().get("report", "No report returned")

            if "news_history" not in st.session_state:
                st.session_state.news_history = []

            st.session_state.news_history.insert(0, {
                "topic": topic,
                "report": report
            })
        else:
            st.error("❌ " + r.text)

# ---------------- RESULTS ----------------
if "news_history" not in st.session_state:
    st.session_state.news_history = []

if st.session_state.news_history:
    st.subheader("📌 Research Reports")

    for item in st.session_state.news_history:
        with st.container(border=True):
            st.markdown("### 🗞 Topic")
            st.info(item["topic"])

            st.markdown("### 📄 AI Research Report")
            st.markdown(item["report"])

else:
    st.info("📰 No research yet. Enter a topic above to begin.")

st.markdown("</div>", unsafe_allow_html=True)

st.divider()
st.caption("⚡ Powered by AURA Multi-Agent AI System")

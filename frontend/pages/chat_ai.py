import streamlit as st
from components.api import api_post_json
from components.ui import load_css

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Chat AI | MULTI USER AI",
    page_icon="💬",
    layout="wide",
    initial_sidebar_state="expanded"
)

load_css()

# ------------------ FORCE FULL BACKGROUND ------------------
st.markdown("""
<style>
/* FULL APP BACKGROUND */
.stApp {
    background: radial-gradient(circle at top left, #0f172a, #020617) !important;
    color: white !important;
}

/* REMOVE WHITE OUTER FRAME */
.main, .block-container {
    background: transparent !important;
}

/* SIDEBAR MATCH */
section[data-testid="stSidebar"] {
    background: radial-gradient(circle at top left, #0f172a, #020617) !important;
}

/* CHAT UI */
.chat-box {
    max-width: 950px;
    margin: auto;
}

div[data-testid="stChatMessage"] {
    background: transparent;
}

div.stChatInput textarea {
    background: rgba(15,23,42,0.85);
    border-radius: 14px;
    border: 1px solid rgba(148,163,184,0.2);
    color: white;
}

div.stChatInput textarea:focus {
    border: 1px solid #38bdf8;
    box-shadow: 0 0 10px rgba(56,189,248,0.3);
}
</style>
""", unsafe_allow_html=True)

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
    <h1>💬 Multi-Agent Chat AI</h1>
    <h4>Persistent memory • Multi-agent reasoning • Real-time AI</h4>
</div>
""", unsafe_allow_html=True)

st.markdown("<div class='chat-box'>", unsafe_allow_html=True)

# ------------------ SESSION ------------------
if "chat" not in st.session_state:
    st.session_state.chat = []

# ------------------ HISTORY ------------------
for m in st.session_state.chat:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

# ------------------ INPUT ------------------
q = st.chat_input("Ask anything...")

if q:
    st.session_state.chat.append({"role": "user", "content": q})

    with st.chat_message("user"):
        st.markdown(q)

    with st.chat_message("assistant"):
        with st.spinner("🧠 Multi-agent system thinking..."):
            r = api_post_json("/chat", {"message": q})

            if r.status_code == 200:
                ans = r.json().get("reply", "No response")
            else:
                ans = f"❌ {r.status_code}\n{r.text}"

            st.markdown(ans)
            st.session_state.chat.append({"role": "assistant", "content": ans})

st.markdown("</div>", unsafe_allow_html=True)

import streamlit as st
from components.ui import load_css
from components.api import api_get, api_post_json

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="AURA Memory Dashboard",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

load_css()

# ------------------ AUTH CHECK ------------------
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
    # st.page_link("pages/memory_dashboard.py", label="🧠 Memory Dashboard")
    st.page_link("pages/document_qa.py", label="📄 Document AI")
    st.page_link("pages/news_research.py", label="📰 News Research")
    st.page_link("pages/youtube_ai.py", label="🎥 YouTube AI")
    st.page_link("pages/About.py", label="ℹ About")
    st.caption("⚡ Powered by FastAPI + LangChain + Groq")
    st.caption("made by Vivek Badgujar")

# ------------------ HERO ------------------
st.markdown("""
<div style="text-align:center; padding:30px 0;">
    <h1>🧠 AI Memory & Logs Center</h1>
    <h4>Complete activity, memory, and intelligence overview</h4>
</div>
""", unsafe_allow_html=True)

# ------------------ CARD STYLE ------------------
st.markdown("""
<style>
.memory-card {
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
# st.markdown("<div class='memory-card'>", unsafe_allow_html=True)

# ---------------- FETCH DATA ----------------
res = api_get("/memory/dashboard")

if res.status_code != 200:
    st.error("❌ Backend not connected or session expired")
    st.stop()

data = res.json()

# ---------------- METRICS ----------------
c1, c2, c3 = st.columns(3)
c1.metric("💬 Total Conversations", data.get("total_chats", 0))
c2.metric("🧠 Stored Memories", data.get("total_memories", 0))
c3.metric("📄 Documents Indexed", data.get("total_docs", 0))

st.divider()

# ---------------- RECENT LOGS ----------------
st.subheader("🕒 Recent AI Activity")

recent = data.get("recent_chats", [])

if not recent:
    st.info("No conversations yet.")
else:
    for chat in recent:
        role = "🧑 User" if chat["role"] == "user" else "🤖 AI"
        with st.container(border=True):
            st.markdown(f"**{role}**")
            st.write(chat["content"])

# ---------------- MEMORY SEARCH ----------------
st.divider()
st.subheader("🔍 Search AI Memory")

query = st.text_input("Search anything the AI remembers")

if query:
    r = api_post_json("/memory/search", {"query": query})

    if r.status_code != 200:
        st.error(r.text)
        st.stop()

    results = r.json().get("results", [])

    if not results:
        st.warning("No matching memory found.")
    else:
        for i, mem in enumerate(results, 1):
            with st.container(border=True):
                st.markdown(f"**{i}.** {mem}")

# ---------------- SYSTEM INFO ----------------
st.divider()
st.subheader("📊 System Coverage")

st.markdown("""
✔ User prompts  
✔ AI replies  
✔ Vector embeddings  
✔ Resume interviews  
✔ Document memory  
✔ News research  
✔ YouTube analysis  
""")

st.success("✅ Memory system active and running")

st.markdown("</div>", unsafe_allow_html=True)

import streamlit as st
from components.api import api_post, api_post_json
from components.ui import load_css

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Document AI | MULTI USER AI",
    page_icon="📄",
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
    # st.page_link("pages/document_qa.py", label="📄 Document AI")
    st.page_link("pages/news_research.py", label="📰 News Research")
    st.page_link("pages/youtube_ai.py", label="🎥 YouTube AI")
    st.page_link("pages/About.py", label="ℹ About")
    st.caption("⚡ Powered by FastAPI + LangChain + Groq")
    st.caption("made by Vivek Badgujar")

# ------------------ HERO ------------------
st.markdown("""
<div style="text-align:center; padding:30px 0;">
    <h1>📄 Document Intelligence System</h1>
    <h4>Upload PDFs • Build knowledge base • Ask AI questions</h4>
</div>
""", unsafe_allow_html=True)

# ------------------ CARD STYLE ------------------
st.markdown("""
<style>
.doc-card {
    background: radial-gradient(circle at top left, #0f172a, #020617);
    border-radius: 22px;
    padding: 30px;
    border: 1px solid rgba(148,163,184,0.15);
    box-shadow: 0 0 35px rgba(56,189,248,0.08);
    max-width: 1100px;
    margin: auto;
}
textarea, input {
    background: rgba(15,23,42,0.9) !important;
    color: white !important;
    border-radius: 12px !important;
    border: 1px solid rgba(148,163,184,0.25) !important;
}
textarea:focus, input:focus {
    border: 1px solid #38bdf8 !important;
    box-shadow: 0 0 12px rgba(56,189,248,0.3) !important;
}
</style>
""", unsafe_allow_html=True)

# ------------------ MAIN CARD ------------------
# st.markdown("<div class='doc-card'>", unsafe_allow_html=True)

# ---------------- UPLOAD ----------------
st.subheader("📤 Upload Document")

doc = st.file_uploader("Upload PDF document", type=["pdf"])

if doc and st.button("🚀 Process Document", use_container_width=True):
    with st.spinner("📄 Processing document... This may take 1–3 minutes."):
        r = api_post("/docs/upload", files={"file": doc})

    if r.status_code == 200:
        st.session_state.doc_id = r.json()["doc_id"]
        st.success("✅ Document processed successfully")
    else:
        st.error(r.text)

# ---------------- ASK ----------------
if "doc_id" in st.session_state:

    st.divider()
    st.subheader("💬 Ask Questions from Document")

    q = st.text_input("Ask anything from this document")

    if q:
        with st.spinner("🤖 Searching and reasoning from document..."):
            r = api_post_json("/docs/ask", {
                "doc_id": st.session_state.doc_id,
                "question": q
            })

        if r.status_code == 200:
            st.markdown("### 🧠 AI Answer")
            st.success(r.json().get("answer", "No answer returned"))
        else:
            st.error(r.text)

st.markdown("</div>", unsafe_allow_html=True)

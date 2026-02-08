import streamlit as st
import time
import io
from components.api import api_post_json, api_get
from components.ui import load_css
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch


# =========================================================
# ---------------- PAGE CONFIG ----------------------------
# =========================================================

st.set_page_config(
    page_title="YouTube AI | MULTI USER AI",
    page_icon="🎥",
    layout="wide",
)

load_css()


# =========================================================
# ---------------- HELPER FUNCTIONS -----------------------
# =========================================================

def format_number(value):
    """Format numbers like 1.2K / 3.4M"""
    if not value:
        return "—"

    try:
        value = int(value)
    except:
        return value

    if value >= 1_000_000:
        return f"{value / 1_000_000:.1f}M"
    if value >= 1_000:
        return f"{value / 1_000:.1f}K"

    return str(value)


def create_pdf(text):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer)
    styles = getSampleStyleSheet()
    story = []

    for line in text.split("\n"):
        story.append(Paragraph(line, styles["Normal"]))
        story.append(Spacer(1, 0.2 * inch))

    doc.build(story)
    buffer.seek(0)
    return buffer


# =========================================================
# ---------------- AUTH CHECK -----------------------------
# =========================================================

if "token" not in st.session_state:
    st.error("🔐 Please login first")
    st.stop()


# =========================================================
# ---------------- USER RESET -----------------------------
# =========================================================

if "last_user" not in st.session_state:
    st.session_state.last_user = st.session_state.current_user

if st.session_state.last_user != st.session_state.current_user:
    for k in [
        "yt_summary",
        "yt_url",
        "processing",
        "stage",
        "last_check",
        "metadata"
    ]:
        if k in st.session_state:
            del st.session_state[k]

    st.session_state.last_user = st.session_state.current_user


# =========================================================
# ---------------- SIDEBAR -------------------------------
# =========================================================

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
    st.caption("Made by Vivek Badgujar")


# =========================================================
# ---------------- PREMIUM CSS ----------------------------
# =========================================================

st.markdown("""
<style>
.big-title {
    font-size: 46px;
    font-weight: 800;
    text-align: center;
}

.sub-title {
    text-align: center;
    color: #9CA3AF;
    margin-bottom: 35px;
}

.glass-card {
    background: rgba(30, 41, 59, 0.6);
    backdrop-filter: blur(12px);
    padding: 30px;
    border-radius: 20px;
    border: 1px solid rgba(255,255,255,0.08);
    box-shadow: 0 0 30px rgba(56,189,248,0.15);
    margin-bottom: 25px;
}
</style>
""", unsafe_allow_html=True)


# =========================================================
# ---------------- HERO SECTION ---------------------------
# =========================================================

st.markdown('<div class="big-title">🎥 YouTube AI</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Quick Summary → Full Summary → Auto Updating</div>', unsafe_allow_html=True)


# =========================================================
# ---------------- INPUT SECTION --------------------------
# =========================================================




url = st.text_input("📎 Paste YouTube Video URL")
generate = st.button("🚀 Generate Summary", use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)


# =========================================================
# ---------------- GENERATE -------------------------------
# =========================================================

if generate:

    if not url.strip():
        st.warning("Please enter a YouTube URL")
        st.stop()

    r = api_post_json("/youtube/summarize", {"url": url})
    data = r.json()

    st.session_state.yt_url = url
    st.session_state.yt_summary = data.get("summary")
    st.session_state.stage = data.get("stage")
    st.session_state.metadata = data.get("metadata")
    st.session_state.processing = True
    st.session_state.last_check = time.time()


# =========================================================
# ---------------- AUTO REFRESH ---------------------------
# =========================================================

if st.session_state.get("processing"):

    if time.time() - st.session_state.get("last_check", 0) > 5:

        r = api_get(f"/youtube/status?url={st.session_state.yt_url}")
        data = r.json()

        st.session_state.yt_summary = data.get("summary")
        st.session_state.stage = data.get("stage")
        st.session_state.metadata = data.get("metadata")
        st.session_state.last_check = time.time()

        if data.get("status") == "done":
            st.session_state.processing = False


# =========================================================
# ---------------- STATUS DISPLAY -------------------------
# =========================================================

stage_map = {
    "quick_summary": "⚡ Creating quick summary...",
    "full_summary": "🧠 Generating detailed summary...",
    "completed": "✅ Summary completed",
    "error": "❌ Error occurred"
}

if st.session_state.get("stage"):
    st.info(stage_map.get(st.session_state.stage))


# =========================================================
# ---------------- METADATA CARD --------------------------
# =========================================================

if st.session_state.get("metadata"):

    meta = st.session_state.metadata

    


    col1, col2 = st.columns([1, 2])

    with col1:
        if meta.get("thumbnail"):
            st.image(meta["thumbnail"], use_container_width=True)

    with col2:
        st.markdown(f"### {meta.get('title')}")
        st.markdown(f"📺 {meta.get('channel')}")
        st.markdown(f"⏱ Duration: {meta.get('duration')}")

        m1, m2, m3 = st.columns(3)

        with m1:
            st.metric("👁 Views", format_number(meta.get("views")))

        with m2:
            st.metric("👍 Likes", format_number(meta.get("likes")))

        with m3:
            st.metric("👥 Subs", format_number(meta.get("subscribers")))

    st.markdown('</div>', unsafe_allow_html=True)


# =========================================================
# ---------------- SUMMARY SECTION ------------------------
# =========================================================

if st.session_state.get("yt_summary"):

    


    st.subheader("📄 AI Summary")

    show_transcript = st.toggle("📜 Show Raw Transcript")

    if show_transcript:
        st.text_area("Transcript", st.session_state.yt_summary, height=250)
    else:
        st.markdown(st.session_state.yt_summary)

    pdf_file = create_pdf(st.session_state.yt_summary)

    st.download_button(
        "📥 Download Summary as PDF",
        data=pdf_file,
        file_name="youtube_summary.pdf",
        mime="application/pdf",
        use_container_width=True
    )

    st.markdown('</div>', unsafe_allow_html=True)

import streamlit as st
from components.api import api_post_json

# ---------------- CONFIG ----------------
st.set_page_config("AI News Researcher | AURA", layout="wide")

# ---------------- GLOBAL STYLE ----------------
st.markdown("""
<style>
.stApp {
    background: radial-gradient(circle at top left, #020617, #020617);
    color: white;
}

.section-card {
    background: rgba(15,23,42,0.85);
    border-radius: 22px;
    padding: 28px;
    border: 1px solid rgba(148,163,184,0.15);
    box-shadow: 0 0 40px rgba(56,189,248,0.08);
    margin-bottom: 25px;
}

.title {
    font-size: 42px;
    font-weight: 800;
}

.subtitle {
    color: #94a3b8;
    font-size: 18px;
}

.report-box {
    background: rgba(2,6,23,0.7);
    border-radius: 18px;
    padding: 22px;
    border: 1px solid rgba(148,163,184,0.12);
}
</style>
""", unsafe_allow_html=True)

# ---------------- AUTH ----------------
if "token" not in st.session_state:
    st.error("🔐 Please login first")
    st.stop()

# ---------------- HEADER ----------------
st.markdown("<div class='title'>📰 AI News Researcher</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Multi-agent system to research, analyze, and summarize live news topics</div>", unsafe_allow_html=True)

st.divider()

# ---------------- INPUT CARD ----------------
# st.markdown("<div class='section-card'>", unsafe_allow_html=True)
st.markdown("## 🔎 Start New Research")

c1, c2 = st.columns([4, 1])

with c1:
    topic = st.text_input(
        "Research topic",
        placeholder="Artificial Intelligence in healthcare, ISRO missions, OpenAI, stock market trends..."
    )

with c2:
    search_btn = st.button("🚀 Research", use_container_width=True)

# st.markdown("</div>", unsafe_allow_html=True)

# ---------------- PROCESS ----------------
if topic and search_btn:
    with st.spinner("🧠 AI agents are scanning, analyzing, and summarizing the news..."):
        r = api_post_json("/agent/news", {"topic": topic})

        if r.status_code == 200:
            report = r.json().get("report", "No report returned")

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

# ---------------- FOOTER ----------------
st.divider()
st.caption("⚡ Powered by AURA Multi-Agent AI System")

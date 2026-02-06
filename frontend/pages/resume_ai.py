import streamlit as st
from components.api import api_post, api_post_json
from components.ui import load_css

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Resume AI | MULTI USER AI",
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
    # st.page_link("pages/resume_ai.py", label="📄 Resume AI")
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
    <h1>📄 Resume Intelligence System</h1>
    <h4>Multi-Stage AI Resume Understanding & Interview Engine</h4>
</div>
""", unsafe_allow_html=True)

# ------------------ CARD STYLE ------------------
st.markdown("""
<style>
.resume-card {
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
# st.markdown("<div class='resume-card'>", unsafe_allow_html=True)

# ================= INPUT =================
st.subheader("📤 Upload your resume (PDF only)")
role = st.text_input("🎯 Target Job Role (e.g. Backend Developer, Data Scientist)")
file = st.file_uploader("Choose resume file", type=["pdf"])

if st.button("🚀 Analyze Resume", use_container_width=True):

    if not file or not role:
        st.warning("Please upload resume and enter role.")
        st.stop()

    with st.spinner("Running AI resume intelligence pipeline..."):
        r = api_post("/resume/process", files={"file": file}, data={"role": role})

    if r.status_code != 200:
        st.error(r.text)
        st.stop()

    st.session_state.resume_data = r.json()
    st.session_state.role = role
    st.success("✅ Resume processed successfully")

# ================= DISPLAY =================
if "resume_data" in st.session_state:

    data = st.session_state.resume_data
    scores = data.get("scores", {})

    st.divider()
    st.subheader("📊 Resume Intelligence Report")

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("📄 Sections", len(data.get("sections", [])))
    c2.metric("🧠 Skills", len(data.get("skills", [])))
    c3.metric("⏳ Experience", data.get("experience_years", 0))
    c4.metric("⭐ Final Score", scores.get("Final", "N/A"))

    st.subheader("📑 Sections")
    if data.get("sections"):
        st.success(" • ".join(data["sections"]))
    else:
        st.info("No sections detected")

    st.subheader("🛠 Skills")
    if data.get("skills"):
        st.write(" • ".join(data["skills"]))
    else:
        st.warning("No skills extracted")

    st.subheader("🚀 Projects / Work Evidence")
    if data.get("projects"):
        for p in data["projects"]:
            with st.container(border=True):
                st.markdown(f"### {p.get('name','Project')}")
                st.write("**Tech:**", ", ".join(p.get("tech", [])))
                st.info(p.get("impact", "No description"))
    else:
        st.warning("No structured projects detected")

    st.divider()
    st.subheader("🎯 Target Role Intelligence")
    role_data = data.get("role_profile", {})

    if role_data.get("role_summary"):
        st.info(role_data["role_summary"])

    r1, r2, r3 = st.columns(3)

    with r1:
        st.markdown("### 🧠 Core Skills")
        for s in role_data.get("core_skills", []):
            st.success(f"✓ {s}")

    with r2:
        st.markdown("### 🛠 Tools & Stack")
        for t in role_data.get("tools", []):
            st.info(f"🔹 {t}")

    with r3:
        st.markdown("### ⭐ Nice to Have")
        for n in role_data.get("nice_to_have", []):
            st.warning(f"＋ {n}")

    if role_data.get("seniority"):
        st.success("🎖 Expected Seniority: " + role_data["seniority"].upper())

    st.divider()
    st.subheader("⚠ Skill Gap Intelligence")

    gaps = data.get("skill_gaps", {})
    missing = gaps.get("missing_core", [])
    weak = gaps.get("weak", [])
    next_level = gaps.get("next_level", [])

    g1, g2, g3 = st.columns(3)

    with g1:
        st.error("❌ Missing Core Skills")
        for s in missing or ["None 🎉"]:
            st.markdown(f"• {s}")

    with g2:
        st.warning("⚠ Weak Skills")
        for s in weak or ["None"]:
            st.markdown(f"• {s}")

    with g3:
        st.success("🚀 Next-Level Skills")
        for s in next_level or ["Already advanced 🚀"]:
            st.markdown(f"• {s}")

    st.divider()
    st.subheader("🤖 Expert Resume Evaluation")
    st.markdown(data.get("ai_summary", "No expert analysis generated."))

    st.divider()
    st.subheader("🎤 AI Interview Generator")

    iq = data.get("interview_questions", {})

    with st.expander("📘 Common Questions"):
        for q in iq.get("common_questions", []):
            st.write("•", q)

    with st.expander("🤖 Resume Based"):
        st.markdown(iq.get("resume_based", "Not generated"))

    with st.expander("🎯 Skill Based"):
        st.markdown(iq.get("skill_based", "Not generated"))

    with st.expander("⚠ Gap Based"):
        st.markdown(iq.get("gap_based", "Not generated"))

    st.divider()
    if st.button("🔁 Generate More AI Questions", use_container_width=True):
        with st.spinner("Advanced interviewer agent working..."):
            r = api_post_json("/resume/more-questions", {
                "stage2": data.get("stage2"),
                "role": st.session_state.role
            })

        if r.status_code == 200:
            st.session_state.more_questions = r.json().get("questions", "")
        else:
            st.error(r.text)

    if "more_questions" in st.session_state:
        st.subheader("🧠 Additional AI Interview Questions")
        st.markdown(st.session_state.more_questions)

    st.success("✅ Resume intelligence pipeline completed")

st.markdown("</div>", unsafe_allow_html=True)

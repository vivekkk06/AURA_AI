import streamlit as st

# ---------------- CONFIG ----------------
st.set_page_config("About | AURA AI", layout="wide")

# ---------------- GLOBAL BACKGROUND ----------------
st.markdown("""
<style>
.stApp {
    background: radial-gradient(circle at top left, #0f172a, #020617);
    color: white;
}

.block-container {
    padding-top: 2rem;
}

.glass {
    background: rgba(15, 23, 42, 0.65);
    backdrop-filter: blur(14px);
    border-radius: 18px;
    padding: 28px;
    border: 1px solid rgba(148,163,184,0.15);
    box-shadow: 0 0 30px rgba(56,189,248,0.08);
    margin-bottom: 28px;
}

.section-title {
    font-size: 30px;
    font-weight: 800;
}

.soft {
    color: #94a3b8;
    font-size: 17px;
    line-height: 1.6;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("""
<div style="text-align:center; padding:25px 0 15px 0;">
    <h1>ℹ About AURA AI</h1>
    <p class="soft">A full-stack, multi-agent, industry-grade Generative AI engineering platform</p>
</div>
""", unsafe_allow_html=True)

st.divider()

# ---------------- ABOUT ----------------
st.markdown("""
<div class="glass">
    <div class="section-title">🧠 What is AURA AI?</div>
    <p class="soft">
        <b>AURA AI</b> is an advanced, production-style <b>multi-user Generative AI platform</b> built to demonstrate
        real-world AI system engineering — not just chatbots.
        <br><br>
        It integrates <b>LLMs, agents, tools, vector search, document intelligence, resume analysis, news research,
        and YouTube understanding</b> into a single unified AI ecosystem.
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
        • Secure JWT authentication system
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
        • Memory Dashboard & vector recall system
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
    AURA AI was built to showcase:
    <br><br>
    ✔ Real-world AI engineering workflows<br>
    ✔ End-to-end GenAI product design<br>
    ✔ Multi-agent system thinking<br>
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
st.success("AURA AI is built as a professional-grade AI engineering platform demonstrating modern GenAI system design.")

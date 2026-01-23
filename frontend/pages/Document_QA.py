import streamlit as st
from components.api import api_post, api_post_json

# ---------------- CONFIG ----------------
st.set_page_config("Document AI | MULTI USER AI", layout="wide")

# ---------------- GLOBAL STYLE ----------------
st.markdown("""
<style>
.stApp {
    background: radial-gradient(circle at top left, #0f172a, #020617);
    color: white;
}

.block-container {
    padding-top: 1.5rem;
    max-width: 1100px;
}

.doc-title {
    font-size: 40px;
    font-weight: 800;
    text-align: center;
}

.doc-sub {
    text-align: center;
    color: #94a3b8;
    margin-bottom: 30px;
}

.doc-card {
    background: rgba(15,23,42,0.7);
    border-radius: 20px;
    padding: 25px;
    border: 1px solid rgba(148,163,184,0.15);
    box-shadow: 0 0 35px rgba(56,189,248,0.08);
    margin-bottom: 25px;
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
# ---------------- HEADER ----------------
st.markdown("""
<div class="doc-title">📄 Document Intelligence System</div>
<div class="doc-sub">Upload PDFs • Build knowledge base • Ask AI questions</div>
""", unsafe_allow_html=True)

# ---------------- AUTH ----------------
if "token" not in st.session_state:
    st.error("🔐 Please login first")
    st.stop()


# ---------------- UPLOAD ----------------
# st.markdown("<div class='doc-card'>", unsafe_allow_html=True)
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

st.markdown("</div>", unsafe_allow_html=True)

# ---------------- ASK ----------------
if "doc_id" in st.session_state:

    # st.markdown("<div class='doc-card'>", unsafe_allow_html=True)
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

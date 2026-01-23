import os
from langchain_groq import ChatGroq

# =========================
# LLM CONFIG
# =========================

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.3,
    groq_api_key=os.getenv("GROQ_API_KEY")
)

# ======================================================
# MULTI-AGENT GENERAL CHAT SYSTEM
# ======================================================

def run_multi_agent(user_id: str, task: str):
    prompt = f"""
You are an intelligent multi-agent AI system.

User ID: {user_id}

Task:
{task}

Think step-by-step and provide a helpful, accurate response.
"""
    return llm.invoke(prompt).content


# ======================================================
# DOCUMENT QUESTION ANSWERING
# ======================================================

def llm_answer_from_context(context: str, question: str):
    prompt = f"""
You are a document assistant.

Rules:
- Use ONLY the context below.
- If the answer is not in the context, say exactly:
  "Not present in the document."

Context:
{context}

Question:
{question}
"""
    return llm.invoke(prompt).content


# ======================================================
# NEWS RESEARCH MULTI-AGENT SYSTEM
# ======================================================

def run_news_agents(topic: str):
    # ---------------- RESEARCH AGENT ----------------
    researcher_prompt = f"""
You are a professional news research agent.

Research this topic using your knowledge:

TOPIC: {topic}

Collect:
- important background
- recent or major events
- organizations or people involved
- trusted news websites that normally report this
Include website links.
"""

    research = llm.invoke(researcher_prompt).content

    # ---------------- ANALYST AGENT ----------------
    analyst_prompt = f"""
You are a senior news analyst.

Organize this research clearly:

{research}

Return:
- 5 structured bullet points
- short clear explanation
- a clean list of source links
"""

    analysis = llm.invoke(analyst_prompt).content

    # ---------------- WRITER AGENT ----------------
    writer_prompt = f"""
You are a professional journalist.

Using the information below, write a news-style article.

{analysis}

Rules:
- factual tone
- simple language
- readable structure
- sources at the end
"""

    final_report = llm.invoke(writer_prompt).content

    return {
        "topic": topic,
        "report": final_report
    }

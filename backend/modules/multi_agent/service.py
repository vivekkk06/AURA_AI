from langchain_groq import ChatGroq
import os

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model="llama3-70b-8192"
)

def planner_agent(query: str):
    return llm.invoke(f"Create a step-by-step plan to solve: {query}").content

def research_agent(plan: str):
    return llm.invoke(f"Research and expand this plan:\n{plan}").content

def solver_agent(research: str):
    return llm.invoke(f"Solve the problem using this info:\n{research}").content

def reviewer_agent(answer: str):
    return llm.invoke(f"Improve and verify this final answer:\n{answer}").content

from tools.groq_llm import groq_chat

def planner(task):
    return groq_chat([
        {"role": "system", "content": "You are a task planner AI."},
        {"role": "user", "content": task}
    ])

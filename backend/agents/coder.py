from tools.groq_llm import groq_chat

def coder(plan):
    return groq_chat([
        {"role": "system", "content": "You write code solutions."},
        {"role": "user", "content": plan}
    ])

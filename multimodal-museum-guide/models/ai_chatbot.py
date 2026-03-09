import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=api_key)


def ask_ai(question, context):

    prompt = f"""
You are a helpful museum guide AI.

Artifact info:
{context}

Visitor question:
{question}

Answer clearly.
"""

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
    )

    return completion.choices[0].message.content
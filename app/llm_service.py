import os

from dotenv import load_dotenv
import google.generativeai as genai


load_dotenv()

genai.configure(
    api_key=os.getenv(
        "GEMINI_API_KEY"
    )
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def generate_answer(
    question: str,
    context: str,
    memory=None
):

    prompt = f"""
You are a strict document question-answering assistant.

RULES:

1. Use ONLY the provided context.
2. Never use outside knowledge.
3. Never infer.
4. Never guess.
5. Maximum 3 bullet points.
6. Maximum 60 words.
7. If the answer is not explicitly present in the context, reply exactly:

I don't know based on the provided document.

Context:
{context}

Question:
{question}
"""

    try:

        response = model.generate_content(
            prompt
        )

        return response.text.strip()

    except Exception as e:

        return f"Gemini Error: {str(e)}"
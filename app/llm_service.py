from ollama import chat


def generate_answer(
    question: str,
    context: str,
    memory=""
):

    prompt = f"""
    You are a document question-answering assistant.

    Rules:
    1. Answer ONLY from the provided context.
    2. Keep answers concise and relevant.
    3. Do NOT add information that is not directly related to the question.
    4. If the answer is not present in the context, say:
    "I don't know based on the provided document."

Conversation History:
{memory}

Context:
{context}

Question:
{question}

Answer:
"""

    response = chat(
        model="phi3",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.message.content
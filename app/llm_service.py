from ollama import chat


def generate_answer(
    question: str,
    context: str,
    memory=None
):

    prompt = f"""
You are a strict document question-answering assistant.

Rules:

1. Use ONLY the provided context.
2. Never use outside knowledge.
3. Never infer.
4. Never guess.
5. Return ONLY the answer.
6. Maximum 3 bullet points.
7. Maximum 60 words.
8. If information is not explicitly present, respond exactly:

I don't know based on the provided document.

Context:
{context}

Question:
{question}
"""

    response = chat(
        model="phi3",
        messages=[
            {
                "role": "system",
                "content":
                    "Answer only from the provided context."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        options={
            "temperature": 0,
            "top_p": 0.5,
            "num_predict": 150
        }
    )

    return response.message.content
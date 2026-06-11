from ollama import chat


def generate_answer(
    question: str,
    context: str,
    memory=""
):

    prompt = f"""
You are a helpful assistant.

Use the conversation history and document context.

If the answer is not found in the context,
say "I don't know based on the provided document."

Conversation History:
{memory}

Context:
{context}

Question:
{question}
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
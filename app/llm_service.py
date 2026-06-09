from ollama import chat

def generate_answer(question: str, context: str):
    prompt = f"""Answer the question using only the provided context"

    context: {context}
    Question: {question} """

    response = chat(
        model = "phi3",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return response.message.content
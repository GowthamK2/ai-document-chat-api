from app.llm_service import (
    generate_answer
)

question = "What is FastAPI?"

context = """
FastAPI is a backend framework.
"""

answer = generate_answer(
    question,
    context
)

print(answer)
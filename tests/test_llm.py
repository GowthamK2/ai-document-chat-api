from app.llm_service import generate_answer

context = """ FastAPI is a modern Python web framework.
It is used for building APIs."""

question = "what is FastAPI?"

answer = generate_answer(
    question,
    context
)

print(answer)
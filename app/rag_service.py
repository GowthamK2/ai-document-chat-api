from app.embeddings import get_embedding

from app.chroma_services import(
    search_chunks
)

from app.llm_service import (
    generate_answer
)

def ask_question(question: str):
    query_embedding = get_embedding(
        question
    )

    results = search_chunks(
        query_embedding,
        n_results=3
    )

    context = "\n".join(
        results["documents"][0]
    )

    answer = generate_answer(
        question,
        context
    )

    return {
        "question": question,
        "answer": answer,
        "context": context
    }
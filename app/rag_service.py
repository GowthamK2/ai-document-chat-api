from app.embeddings import get_embedding

from app.chroma_services import (
    search_chunks
)

from app.llm_service import (
    generate_answer
)

from app.memory_service import (
    add_to_memory,
    get_memory
)


def ask_question(question: str):

    memory = get_memory()

    history = ""

    for item in memory:
        history += (
            item["question"] + " "
        )
    enhanced_query = (
        history + question
    )

    query_embedding = get_embedding(
        enhanced_query
    )

    results = search_chunks(
        query_embedding,
        n_results=3
    )

    context = "\n".join(
        results["documents"][0]
    )

    memory = get_memory()

    memory_text = ""

    for item in memory:
        memory_text += (
            f"Question: {item['question']}\n"
            f"Answer: {item['answer']}\n\n"
        )

    answer = generate_answer(
        question,
        context,
        memory_text
    )

    add_to_memory(
        question,
        answer
    )

    return {
        "question": question,
        "answer": answer,
        "context": context
    }
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

from app.evaluation_service import (
    evaluate_response,
    confidence_score
)

from app.hallucination_service import (
    detect_hallucination
)

from app.reranker import (
    rerank_chunks
)



def ask_question(
    question: str
):

    # -------------------------
    # Memory
    # -------------------------

    memory = get_memory()

    # -------------------------
    # Retrieval
    # -------------------------

    query_embedding = get_embedding(
        question
    )

    results = search_chunks(
        query_embedding,
        n_results=3
    )

    # -------------------------
    # No Results Guard
    # -------------------------

    if (
        not results
        or "documents" not in results
        or not results["documents"]
    ):

        return {
            "question": question,
            "answer":
                "I don't know based on the provided document.",
            "context": "",
            "sources": [],
            "evaluation": {},
            "hallucination": {},
            "confidence": 0
        }

    retrieved_chunks = (
        results["documents"][0]
    )

    # -------------------------
    # Reranking
    # -------------------------

    best_chunks = rerank_chunks(
        question,
        retrieved_chunks
    )

    # -------------------------
    # No Relevant Context Guard
    # -------------------------

    if not best_chunks:

        answer = (
            "I don't know based on the provided document."
        )

        context = ""

    else:

        context = "\n\n".join(
            best_chunks
        )

        answer = generate_answer(
            question,
            context,
            memory
        )

    # -------------------------
    # Evaluation
    # -------------------------

    evaluation = evaluate_response(
        question,
        context,
        answer
    )

    hallucination = detect_hallucination(
        answer,
        context
    )

    unsupported_word_count = hallucination.get(
        "unsupported_word_count",
        0
    )

    confidence = confidence_score(
        len(context),
        unsupported_word_count
    )

    # -------------------------
    # Save Memory
    # -------------------------

    add_to_memory(
        question,
        answer
    )

    # -------------------------
    # Response
    # -------------------------

    return {
        "question": question,
        "answer": answer,
        "context": context,
        "sources": best_chunks,
        "retrieved_chunks": len(
            retrieved_chunks
        ),
        "reranked_chunks": len(
            best_chunks
        ),
        "evaluation": evaluation,
        "hallucination": hallucination,
        "confidence": confidence
    }
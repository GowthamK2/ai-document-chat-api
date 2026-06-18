import re


STOP_WORDS = {
    "the", "a", "an",
    "is", "are", "was", "were",
    "which", "what", "who",
    "of", "to", "for",
    "and", "in", "on"
}


def rerank_chunks(
    query: str,
    chunks: list
):

    query_words = {
        word
        for word in re.findall(
            r"\w+",
            query.lower()
        )
        if word not in STOP_WORDS
    }

    scored_chunks = []

    for chunk in chunks:

        chunk_words = {
            word
            for word in re.findall(
                r"\w+",
                chunk.lower()
            )
            if word not in STOP_WORDS
        }

        overlap_score = len(
            query_words.intersection(
                chunk_words
            )
        )

        score = overlap_score

        scored_chunks.append(
            (score, chunk)
        )

    scored_chunks.sort(
        key=lambda x: x[0],
        reverse=True
    )

    best_chunks = [
        chunk
        for score, chunk in scored_chunks
        if score > 0
    ]

    return best_chunks[:2]
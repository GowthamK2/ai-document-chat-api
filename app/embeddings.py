from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def get_embedding(
    text: str
) -> list:

    if not text.strip():

        raise ValueError(
            "Cannot embed empty text."
        )

    embedding = model.encode(
        text,
        normalize_embeddings=True
    )

    return embedding.tolist()


def get_embeddings(
    texts: list
) -> list:

    embeddings = model.encode(
        texts,
        normalize_embeddings=True
    )

    return embeddings.tolist()
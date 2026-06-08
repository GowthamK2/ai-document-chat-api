from app.services.chroma_service import (
    store_chunks,
    collection_count
)

chunks = [
    "FastAPI is a Python web framework.",
    "ChromaDB is a vector database."
]

embeddings = [
    [0.1] * 384,
    [0.2] * 384
]

store_chunks(chunks, embeddings)

print(collection_count())
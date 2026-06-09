from app.chroma_services import (
    store_chunks,
    collection
)

chunks = [
    "FastAPI is a backend framework",
    "ChromaDB is a vector database"
]

embeddings = [
    [0.1] * 384,
    [0.2] * 384
]

store_chunks(
    chunks,
    embeddings
)

print("Total documents:", collection.count())
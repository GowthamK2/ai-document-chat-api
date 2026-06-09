from app.embeddings import get_embedding

from app.chroma_services import (
    search_chunks
)

query = "What is FastAPI?"

query_embedding = get_embedding(
    query
)

results = search_chunks(
    query_embedding
)

print(results)
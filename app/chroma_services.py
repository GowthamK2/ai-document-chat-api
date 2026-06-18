import uuid
import chromadb

client = chromadb.PersistentClient(
    path="data/chroma_db"
)

collection = client.get_or_create_collection(
    name="document"
)


def store_chunks(
    chunks,
    embeddings
):

    ids = [
        str(uuid.uuid4())
        for _ in chunks
    ]

    metadatas = [
        {
            "chunk_number": i
        }
        for i in range(len(chunks))
    ]

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings,
        metadatas=metadatas
    )


def search_chunks(
    query_embedding,
    n_results=3
):

    results = collection.query(
        query_embeddings=[
            query_embedding
        ],
        n_results=n_results,
        include=[
            "documents",
            "distances",
            "metadatas"
        ]
    )

    return results
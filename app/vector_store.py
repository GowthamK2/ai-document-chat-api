import chromadb

client = chromadb.PersistentClient(path = "data/chroma_db")

collection = client.get_or_create_collection(name="document")

def store_chunks(chunks, embeddings):
    ids = [f"chunk__{i}" for i in range(len(chunks))]

    collection.add(
                   ids=ids,
                   documents=chunks,
                   embeddings=embeddings)
    
def search_chunks(query_embedding, n_results=3):
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )
    return results
    
    return results

def collection_count():
    return collection.count()

store_chunks(chunks, embeddings)

print("Stored chunks:", collection_count())


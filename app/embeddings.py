from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

def get_embedding(text: str):
    embedding = model.encode(text)
    return embedding.tolist()

def get_embeddings(texts: list):
    embeddings = model.encode(texts)
    return embeddings.tolist() 
import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from app.embeddings import get_embedding

text = "FastAPI is a backend framework"

embedding = get_embedding(text)

print(type(embedding))
print(len(embedding))
print(embedding[:5])
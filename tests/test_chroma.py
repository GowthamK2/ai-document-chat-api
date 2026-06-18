from app.chroma_services import (
    collection
)

print(
    "Total documents:",
    collection.count()
)
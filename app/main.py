from fastapi import FastAPI
from fastapi import UploadFile, File

from pydantic import BaseModel

from app.rag_service import ask_question

import os

from app.chunker import chunk_text
from app.document_loader import extract_text_from_pdf

from app.embeddings import (
    get_embedding,
    get_embeddings
)

from app.chroma_services import (
    store_chunks,
    search_chunks
)

app = FastAPI(
    title="AI Document Chat API"
)


class SearchRequest(BaseModel):
    query: str

class AskRequest(BaseModel):
    question: str

@app.get("/")
async def home():
    return {
        "message": "AI Document Chat API running"
    }


@app.post("/upload-pdf")
async def upload_pdf(
    file: UploadFile = File(...)
):
    upload_dir = "data/uploads"

    os.makedirs(
        upload_dir,
        exist_ok=True
    )

    file_path = os.path.join(
        upload_dir,
        file.filename
    )

    with open(
        file_path,
        "wb"
    ) as buffer:

        content = await file.read()
        buffer.write(content)

    # Extract text
    text = extract_text_from_pdf(
        file_path
    )

    # Create chunks
    chunks = chunk_text(text)

    # Generate embeddings
    embeddings = get_embeddings(
        chunks
    )

    # Store in ChromaDB
    store_chunks(
        chunks,
        embeddings
    )

    return {
        "filename": file.filename,
        "characters": len(text),
        "total_chunks": len(chunks),
        "stored_in_chromadb": True,
        "first_chunk": chunks[0]
    }


@app.post("/search")
async def search_documents(
    request: SearchRequest
):

    query_embedding = get_embedding(
        request.query
    )

    results = search_chunks(
        query_embedding,
        n_results=3
    )

    return {
        "query": request.query,
        "results": results["documents"][0]
    }

@app.post("/ask")
async def ask(
    request: AskRequest
):
    result = ask_question(request.question)

    return result
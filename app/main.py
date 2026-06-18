from fastapi import FastAPI
from fastapi import UploadFile, File
from pydantic import BaseModel

import os

from app.chunker import chunk_text
from app.document_loader import extract_text_from_pdf
from app.embeddings import get_embedding
from app.chroma_services import (
    store_chunks,
    search_chunks
)
from app.rag_service import ask_question

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

    if not file.filename.endswith(
        ".pdf"
    ):
        return {
            "error":
            "Only PDF files are allowed."
        }

    upload_dir = "data/uploads"

    os.makedirs(
        upload_dir,
        exist_ok=True
    )

    file_path = os.path.join(
        upload_dir,
        file.filename
    )

    try:

        with open(
            file_path,
            "wb"
        ) as buffer:

            content = await file.read()
            buffer.write(content)

        text = extract_text_from_pdf(
            file_path
        )

        chunks = chunk_text(
            text
        )

        embeddings = [
            get_embedding(chunk)
            for chunk in chunks
        ]

        store_chunks(
            chunks,
            embeddings
        )

        first_chunk = (
            chunks[0]
            if chunks
            else ""
        )

        return {
            "filename":
                file.filename,

            "characters":
                len(text),

            "total_chunks":
                len(chunks),

            "first_chunk":
                first_chunk
        }

    except Exception as e:

        return {
            "error": str(e)
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
    return ask_question(
        request.question
    )
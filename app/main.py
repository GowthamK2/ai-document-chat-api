from fastapi import FastAPI

from fastapi import UploadFile , File

import os

from app.chunker import chunk_text

from app.document_loader import (
    extract_text_from_pdf
)

app = FastAPI(
    title="AI Document Chat API"
)

@app.get("/")
async def home():
    return {
        "message": "AI Document chat API running"
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

    text = extract_text_from_pdf(
        file_path
    )

    chunks = chunk_text(text)

    return {
        "filename": file.filename,
        "characters": len(text),
        "total_chunks": len(chunks),
        "first_chunk": chunks[0]
    }
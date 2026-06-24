# 🤖 DocMind AI (AI Document Chat APP)

DocMind AI is a Retrieval-Augmented Generation (RAG) application that allows users to upload PDF documents and ask questions about their content using natural language.

The system combines semantic search, vector embeddings, document retrieval, reranking, and Google Gemini to generate grounded answers from uploaded documents.

---

## 🚀 Features

### 📄 PDF Processing

* Upload PDF documents
* Extract and clean text
* Automatic document chunking

### 🔍 Semantic Search

* Vector embeddings generation
* ChromaDB vector storage
* Similarity-based retrieval

### 🧠 Retrieval-Augmented Generation (RAG)

* Context-aware document question answering
* Retrieval of relevant document chunks
* Response generation using Google Gemini

### 🎯 Reranking

* Keyword-overlap reranking
* Improves retrieval relevance
* Selects best context before generation

### 💬 Conversational Memory

* Maintains recent conversation history
* Supports follow-up questions
* Stores last 5 interactions

### 🛡 Hallucination Detection

* Detects unsupported words in generated responses
* Flags potentially ungrounded answers

### 📊 Confidence Scoring

* Context quality evaluation
* Hallucination-aware confidence calculation

### 🐳 Docker Support

* Fully containerized application
* Production-ready Docker image

---

## 🏗 Architecture

```text
User
 │
 ▼
Streamlit Frontend
 │
 ▼
FastAPI Backend
 │
 ├── PDF Upload
 │
 ├── Text Extraction
 │
 ├── Chunking
 │
 ├── Embeddings
 │
 ├── ChromaDB
 │
 ├── Retrieval
 │
 ├── Reranking
 │
 ├── Gemini LLM
 │
 ├── Hallucination Detection
 │
 └── Confidence Scoring
 │
 ▼
Response
```

---

## 🛠 Tech Stack

### Backend

* Python
* FastAPI
* Pydantic

### Frontend

* Streamlit

### AI & RAG

* Google Gemini API
* ChromaDB
* Sentence Transformers
* Semantic Search
* Retrieval-Augmented Generation (RAG)

### Document Processing

* PyPDF2

### Deployment

* Docker
* GitHub

---

## 📂 Project Structure

```text
ai-document-chat-api/
│
├── app/
│   ├── main.py
│   ├── rag_service.py
│   ├── llm_service.py
│   ├── embeddings.py
│   ├── chroma_services.py
│   ├── document_loader.py
│   ├── chunker.py
│   ├── reranker.py
│   ├── hallucination_service.py
│   ├── evaluation_service.py
│   └── memory_service.py
│
├── frontend/
│   └── app.py
│
├── data/
│   ├── uploads/
│   └── chroma_db/
│
├── tests/
│
├── Dockerfile
├── requirements.txt
├── .dockerignore
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/GowthamK2/ai-document-chat-api.git

cd ai-document-chat-api
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=your_gemini_api_key
```

Get your API key from:

https://aistudio.google.com/

---

## ▶ Running Backend

```bash
uvicorn app.main:app --reload
```

Backend:

```text
http://127.0.0.1:8000
```

Swagger Docs:

```text
http://127.0.0.1:8000/docs
```

---

## ▶ Running Frontend

```bash
streamlit run frontend/app.py
```

Frontend:

```text
http://localhost:8501
```

---

## 🐳 Docker

### Build Image

```bash
docker build -t docmind-ai .
```

### Run Container

```bash
docker run -p 8080:8080 docmind-ai
```

API:

```text
http://localhost:8080/docs
```

---

## 📡 API Endpoints

### Upload PDF

```http
POST /upload-pdf
```

Upload and process PDF documents.

### Search Documents

```http
POST /search
```

Retrieve relevant document chunks.

### Ask Questions

```http
POST /ask
```

Ask questions about uploaded documents.

---

## 📊 Evaluation Metrics

The system evaluates every response using:

### Context Length

Amount of retrieved context used.

### Answer Length

Generated response length.

### Hallucination Score

Unsupported words compared to retrieved context.

### Confidence Score

Combined retrieval and hallucination quality metric.

---

## 📸 Sample Use Cases

### Resume Question Answering

```text
What skills does Gowtham have?
```

### Education Extraction

```text
What is Gowtham's education?
```

### Certification Search

```text
Has Gowtham completed any certifications?
```

### Project Retrieval

```text
What projects has Gowtham worked on?
```

---

## ⚠ Current Limitations

* Uses local SentenceTransformer embeddings.
* Free-tier cloud deployments may face memory limitations.
* Pronoun resolution for follow-up questions is limited.
* ChromaDB is currently configured for local persistence.

### Future Improvements

* Gemini Embeddings
* Hybrid Search
* Query Rewriting
* Cloud Deployment
* Multi-document Support
* Authentication & User Accounts
* AWS/GCP Production Deployment

---

## 👨‍💻 Author

**Gowtham K**

B.Tech – Artificial Intelligence & Machine Learning

GitHub:
https://github.com/GowthamK2

---

## ⭐ Project Highlights

* End-to-End RAG System
* Gemini-Powered Question Answering
* Vector Search with ChromaDB
* Hallucination Detection
* Confidence Scoring
* Dockerized Architecture
* Production-Oriented Design

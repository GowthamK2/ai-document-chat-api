import streamlit as st
import requests

BACKEND_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="AI Document Chat",
    page_icon="🤖"
)

st.title("🤖 AI Document Chat")

st.write(
    "Upload a PDF and chat with it"
)

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file:
    files = {
        "file": (
            uploaded_file.name,
            uploaded_file,
            "application/pdf"
        )
    }

    if st.button("Process PDF"):

        response = requests.post(
            f"{BACKEND_URL}/upload-pdf",
            files=files
        )

        if response.status_code == 200:

            st.success(
                "PDF uploaded successfully!"
            )

            st.json(
                response.json()
            )

question = st.text_input(
    "Ask a question"
)

if st.button("Ask"):

    response = requests.post(
        f"{BACKEND_URL}/ask",
        json={
            "question": question
        }
    )

    if response.status_code == 200:

        result = response.json()

        st.subheader("Answer")

        st.write(
            result["answer"]
        )

        st.subheader(
            "Evaluation"
        )

        st.json(
            result["evaluation"]
        )

        st.subheader(
            "Hallucination"
        )

        st.json(
            result["hallucination"]
        )

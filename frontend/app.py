import streamlit as st
import requests

BACKEND_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="DocMind AI",
    page_icon="🤖",
    layout="wide"
)

# -----------------------------
# Session State
# -----------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------------
# Sidebar
# -----------------------------

with st.sidebar:

    st.title("📄 Document Upload")

    # Backend Status

    try:

        requests.get(
            f"{BACKEND_URL}/",
            timeout=2
        )

        st.success(
            "🟢 Backend Connected"
        )

    except Exception:

        st.error(
            "🔴 Backend Offline"
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

            try:

                with st.spinner(
                    "Processing PDF..."
                ):

                    response = requests.post(
                        f"{BACKEND_URL}/upload-pdf",
                        files=files
                    )

                if response.status_code == 200:

                    st.success(
                        "✅ PDF Processed Successfully!"
                    )

                else:

                    st.error(
                        "Failed to process PDF"
                    )

            except Exception as e:

                st.error(
                    f"Backend Error: {e}"
                )

    st.divider()

    # Conversation History

    st.subheader(
        "📝 Conversation History"
    )

    if not st.session_state.messages:

        st.caption(
            "No conversations yet"
        )

    else:

        for msg in st.session_state.messages:

            if msg["role"] == "user":

                st.write(
                    "🧑 " + msg["content"]
                )

    st.divider()

    # Clear Chat

    if st.button(
        "🗑 Clear Chat"
    ):

        st.session_state.messages = []

        st.rerun()

# -----------------------------
# Main UI
# -----------------------------

st.title("🤖 DocMind AI")

st.caption(
    "Conversational RAG powered by FastAPI, ChromaDB and Phi-3"
)

# Display Previous Messages

for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):

        st.markdown(
            message["content"]
        )

# -----------------------------
# Chat Input
# -----------------------------

question = st.chat_input(
    "Ask a question about your document..."
)

if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message(
        "user"
    ):
        st.markdown(question)

    try:

        with st.spinner(
            "Thinking..."
        ):

            response = requests.post(
                f"{BACKEND_URL}/ask",
                json={
                    "question": question
                }
            )

            result = response.json()

        answer = result["answer"]

        evaluation = result["evaluation"]

        hallucination = result["hallucination"]

        confidence = result.get(
            "confidence",
            0
        )

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

        with st.chat_message(
            "assistant"
        ):

            st.markdown(answer)

            # Metrics

            col1, col2, col3, col4 = st.columns(4)

            with col1:

                st.metric(
                    "Context",
                    evaluation.get(
                        "context_length",
                        0
                    )
                )

            with col2:

                st.metric(
                    "Answer",
                    evaluation.get(
                        "answer_length",
                        0
                    )
                )

            with col3:

                st.metric(
                    "Hallucination",
                    hallucination.get(
                        "unsupported_word_count",
                        0
                    )
                )

            with col4:

                st.metric(
                    "Confidence",
                    f"{confidence}%"
                )

            # Hallucination Status

            if hallucination.get(
                "possible_hallucination",
                False
            ):

                st.warning(
                    "⚠ Possible Hallucination"
                )

            else:

                st.success(
                    "✅ Grounded Response"
                )

            # Sources

            with st.expander(
                "📚 Sources Used"
            ):

                sources = result.get(
                    "sources",
                    []
                )

                if not sources:

                    st.write(
                        "No sources available"
                    )

                else:

                    for source in sources:

                        st.markdown("---")

                        st.write(
                            source
                        )

    except Exception as e:

        st.error(
            f"Backend Error: {e}"
        )
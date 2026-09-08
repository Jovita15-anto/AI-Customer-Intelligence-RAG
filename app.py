import streamlit as st
import os

from sqlrag import initialize_database, build_vector_index, hybrid_rag


st.set_page_config(
    page_title="AI Customer Intelligence Assistant",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 AI Customer Intelligence Assistant")

st.write(
    "Upload a SQLite database and ask questions about your customer data."
)

uploaded_file = st.file_uploader(
    "Upload SQLite Database",
    type=["db", "sqlite", "sqlite3"]
)

if uploaded_file is not None:

    database_path = "uploaded_database.db"

    with open(database_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    initialize_database(database_path)

    build_vector_index()

    st.success("Database uploaded and indexed successfully!")

    question = st.text_area(
        "Ask a question about your database:",
        placeholder="Example: Which Bangalore customers had delivery issues?",
        height=100
    )

    if st.button("Ask Question"):

        if not question.strip():
            st.warning("Please enter a question.")

        else:
            with st.spinner("Analyzing your question..."):

                answer = hybrid_rag(question)

            st.subheader("Answer")
            st.write(answer)
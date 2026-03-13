import streamlit as st
from rag_pipeline import search_documents

st.title("AI Customer Support Copilot")

st.write("Ask questions about customer support documents.")

question = st.text_input("Enter your question")

if question:
    result = search_documents(question)

    st.subheader("Answer")
    st.write(result)

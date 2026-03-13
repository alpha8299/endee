import streamlit as st

st.title("AI Customer Support Copilot")

st.write("Ask questions about support documents.")

question = st.text_input("Enter your question")

if question:
    st.write("Searching knowledge base...")
    st.write("Answer will appear here")

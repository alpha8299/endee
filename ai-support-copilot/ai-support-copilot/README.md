⚠️ Project Location

This repository is forked from the official Endee vector database repository.

My AI/ML project implementation can be found in the folder:

ai-support-copilot/ai-support-copilot

That folder contains the main project files:

- app.py – main application
- rag_pipeline.py – RAG pipeline logic
- knowledge_base.txt – knowledge base data
- requirements.txt – project dependencies
# AI Customer Support Copilot (RAG Based)

## Project Overview

Customer support teams usually manage a large amount of documentation such as FAQs, troubleshooting guides, and help manuals. Finding the correct information from these documents can take time, especially when users ask questions in different ways.

This project implements a simple **AI Customer Support Copilot** that helps retrieve relevant answers from a knowledge base using a Retrieval Augmented Generation (RAG) style workflow. Instead of relying only on keyword matching, the system converts documents and queries into embeddings and performs semantic similarity search to find the most relevant response.

The goal of this project is to demonstrate how modern AI systems can combine **embeddings, semantic search, and a knowledge base** to build an intelligent support assistant.

---

## Problem Statement

In many organizations, support agents must search through multiple documents to answer common customer queries such as password reset instructions, account settings help, or subscription management.

Traditional search systems depend on exact keywords, which often fail when users phrase their questions differently. A more intelligent system should understand the **meaning of the query** and retrieve the most relevant information.

---

## Proposed Solution

This project uses a lightweight RAG pipeline that:

1. Stores support information in a knowledge base.
2. Converts the text into vector embeddings using a sentence transformer model.
3. Converts the user's question into an embedding.
4. Performs vector similarity search to identify the most relevant document.
5. Returns the best matching answer through a simple interface.

This approach allows the system to retrieve answers based on **semantic meaning instead of exact keywords**.

---

## Key Features

* Semantic search using sentence embeddings
* Simple RAG-style retrieval pipeline
* Customer support knowledge base
* Lightweight and easy to extend
* Interactive interface for asking questions

---

## Tech Stack

* Python
* Sentence Transformers
* NumPy
* Streamlit (for the user interface)

---

## System Architecture

User Query
↓
Sentence Embedding Model
↓
Vector Similarity Search
↓
Retrieve Relevant Knowledge Base Entry
↓
Display Best Matching Answer

---

## Example Use Case

User Question:
"How can I reset my password?"

System Response:
The system searches the knowledge base and returns the relevant support instruction for resetting the password.

---

## Future Improvements

Some improvements that could make the system more powerful include:

* Support for larger document collections
* Integration with a vector database
* Multi-document retrieval and ranking
* More advanced language model based response generation

---

## Conclusion

This project demonstrates how semantic search and a simple RAG workflow can be used to build a helpful AI support assistant. Even with a small knowledge base, the system shows how embeddings can improve information retrieval and make support systems more intelligent and efficient.

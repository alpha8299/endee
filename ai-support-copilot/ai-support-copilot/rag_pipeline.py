from sentence_transformers import SentenceTransformer
import numpy as np

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load knowledge base documents
with open("knowledge_base.txt", "r") as f:
    documents = f.readlines()

documents = [doc.strip() for doc in documents if doc.strip() != ""]

# Create embeddings for documents
doc_embeddings = model.encode(documents)

def search_documents(query):
    query_embedding = model.encode(query)

    similarities = np.dot(doc_embeddings, query_embedding)

    best_index = similarities.argmax()

    return documents[best_index]

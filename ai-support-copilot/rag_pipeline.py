from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

documents = [
    "To reset your password, click on Forgot Password on the login page.",
    "You can cancel your subscription from the account settings page.",
    "For payment issues contact support@example.com."
]

doc_embeddings = model.encode(documents)

def search_documents(query):
    query_embedding = model.encode(query)

    similarities = np.dot(doc_embeddings, query_embedding)

    best_index = similarities.argmax()

    return documents[best_index]

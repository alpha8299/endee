from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def create_embedding(text):
    return model.encode(text)

def search_vector(query_embedding):
    # here Endee vector search will happen
    return "Relevant document chunk"

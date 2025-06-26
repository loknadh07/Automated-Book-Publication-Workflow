import chromadb
from chromadb.utils import embedding_functions
import os

# Create persistent directory if it doesn't exist
persist_dir = "./chroma_store"
os.makedirs(persist_dir, exist_ok=True)

# Use new style Chroma client
client = chromadb.PersistentClient(path=persist_dir)

embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

collection = client.get_or_create_collection(
    name="book_versions",
    embedding_function=embedding_fn
)

# Load and split into paragraphs
def load_paragraphs(filepath, label):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    paragraphs = [p.strip() for p in content.split("\n\n") if p.strip()]
    return [
        {"id": f"{label}_p{i}", "doc": p, "meta": {"type": label, "paragraph": i}}
        for i, p in enumerate(paragraphs)
    ]

all_items = (
    load_paragraphs("chapter1.txt", "original") +
    load_paragraphs("chapter1_ai.txt", "ai") +
    load_paragraphs("chapter1_final.txt", "final")
)

docs = [item["doc"] for item in all_items]
ids = [item["id"] for item in all_items]
metas = [item["meta"] for item in all_items]

collection.add(documents=docs, ids=ids, metadatas=metas)

print("✅ All paragraphs stored.")
print("Total chunks:", len(docs))

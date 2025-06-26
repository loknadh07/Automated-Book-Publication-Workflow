import chromadb
from chromadb.utils import embedding_functions

# Connect to the same persistent directory
client = chromadb.PersistentClient(path="./chroma_store")

# Load embedding function
embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

# Get the collection
collection = client.get_or_create_collection(
    name="book_versions",
    embedding_function=embedding_fn
)

# Fetch records
records = collection.get()

print(f"\n✅ Total Documents in DB: {len(records['documents'])}")
print("👉 Sample Metadata + Snippet:")

for i in range(min(3, len(records['documents']))):
    print(f"ID: {records['ids'][i]}")
    print(f"Type: {records['metadatas'][i].get('type')}")
    print(f"Content: {records['documents'][i][:100]}...\n")

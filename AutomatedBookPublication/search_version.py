import chromadb
from chromadb.utils import embedding_functions

# Connect to persistent DB
client = chromadb.PersistentClient(path="./chroma_store")

# Use the same embedding model
embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

# Get the collection
collection = client.get_or_create_collection(
    name="book_versions",
    embedding_function=embedding_fn
)

# Ask user for query
query = input("🔍 Ask something (e.g., 'How does the story begin?'): ")

# Perform search
results = collection.query(
    query_texts=[query],
    n_results=1
)

# Display result
if results["documents"] and results["documents"][0]:
    print("\n📄 Best Matching Version:")
    print("Type:", results["metadatas"][0][0]["type"])
    print("------ Content Snippet ------")
    print(results["documents"][0][0][:1000], "...\n")
else:
    print("⚠️ No matching content found. Try a simpler or different query.")

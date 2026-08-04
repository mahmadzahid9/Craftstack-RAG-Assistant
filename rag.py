import chromadb
from sentence_transformers import SentenceTransformer

VECTOR_DB_DIR = "vector_db"

# Load embedding model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# Connect to ChromaDB
client = chromadb.PersistentClient(path=VECTOR_DB_DIR)

collection = client.get_collection("documents")


def retrieve_with_relevance(query, top_k=3, threshold=1.20):
    print(f"\n=== [Stage 5: Retrieval] Querying Vector DB for: '{query}' ===")
    try:
        total_docs = collection.count()
        print(f"[Stage 5: Retrieval] Total documents in collection: {total_docs}")
        if total_docs == 0:
            print("[Stage 5: Retrieval] WARNING: Search collection is empty.")
            return False, ""

        query_embedding = embedding_model.encode(query).tolist()
        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )

        if not results or not results["documents"] or len(results["documents"][0]) == 0:
            print("[Stage 5: Retrieval] No chunks matched the query.")
            return False, ""

        retrieved_docs = results["documents"][0]
        distances = results["distances"][0] if "distances" in results else []
        
        print(f"[Stage 5: Retrieval] Retrieved {len(retrieved_docs)} chunks.")
        
        for idx, (doc, dist) in enumerate(zip(retrieved_docs, distances)):
            print(f"  Chunk {idx+1}:")
            print(f"    Distance score (lower is closer): {dist:.4f}")
            print(f"    Content snippet: {repr(doc[:150])}")

        top_distance = distances[0] if distances else 999.0
        is_relevant = top_distance < threshold
        print(f"[Stage 5: Retrieval] Top match distance: {top_distance:.4f} (threshold: {threshold}) -> Is Relevant? {is_relevant}")

        context = "\n\n".join(retrieved_docs)
        return is_relevant, context
    except Exception as e:
        print(f"[Stage 5: Retrieval] ERROR: Retrieval failed: {e}")
        return False, ""


def retrieve(query, top_k=3):
    # Always return context when calling direct retrieve (threshold set to 999.0)
    _, context = retrieve_with_relevance(query, top_k=top_k, threshold=999.0)
    return context
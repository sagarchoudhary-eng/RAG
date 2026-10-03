import chromadb
from generation.reranker import rerank
from embeddings.embedder import generate_embedding

chroma = chromadb.PersistentClient(path="./data/chroma")
collection = chroma.get_or_create_collection(name="doc_search")

def add_chunks_to_collection(chunks, embeddings):
    collection.add(
        ids=[chunk["chunk_id"] for chunk in chunks],
        documents=[chunk["text"] for chunk in chunks],
        embeddings=embeddings,
        metadatas=[
            {
                "document_id": chunk["document_id"],
                "page_number": chunk["page_number"],
                "chunk_index": chunk["chunk_index"]
            }
            for chunk in chunks
        ]
    )

def search(query: str, top_k: int = 5):
    # 1. Convert user query into the same 384D embedding
    query_embedding = generate_embedding(query)

    # 2. Search Chroma using the query embedding
    results = collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=top_k
    )

    # 3. Convert Chroma's response into a cleaner structure
    search_results = []

    for i in range(len(results["ids"][0])):
        search_results.append({
            "chunk_id": results["ids"][0][i],
            "text": results["documents"][0][i],
            "page_number": results["metadatas"][0][i]["page_number"],
            "document_id": results["metadatas"][0][i]["document_id"],
            "distance": results["distances"][0][i]
        })

    return search_results

def context_builder(query: str, top_k: int = 5):
    search_results = search(query, top_k=20)

    reranked_results = rerank(
            query,
            search_results,
            top_k=5
        )
    context = ""
    sources = []
    for i, result in enumerate(reranked_results, start=1):
        page_number = int(result["page_number"])
        text = result["text"].replace("\n", " ")

        context += (
            f"[Source {i} | Page {page_number}]\n"
            f"{text}\n\n"
        )

        sources.append({
            "source": i,
            "chunk_id": result["chunk_id"],
            "document_id": result["document_id"],
            "page_number": page_number,
            "distance": result["distance"],
            "rerank_score": result["rerank_score"]
        })
    return context , sources

        
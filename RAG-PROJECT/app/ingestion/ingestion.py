from loader import load_document
from chunker import chunk_text
from pathlib import Path
from embeddings.embedder import generate_embedding
from vectorstore.chroma_store import add_chunks_to_collection, search , context_builder
from generation.llm import generate_answer
from generation.reranker import rerank


def ingest_document():
    path = Path("D:\\python\\RAG-PROJECT\\data\\documents\\O'Reilly Kubernetes Up and Running.pdf")
    document_id = path.stem  # Use the file name without extension as document_id

    pages = load_document(
        "D:\\python\\RAG-PROJECT\\data\\documents\\O'Reilly Kubernetes Up and Running.pdf"
    )

    chunks = chunk_text(pages,document_id=document_id)
    embeddings = [generate_embedding(chunk["text"]) for chunk in chunks]

    add_chunks_to_collection(chunks,embeddings)

    print("Chunks:", len(chunks))
    print("Embeddings:", len(embeddings))
    print("Embedding dimension:", len(embeddings[0]))

if __name__ == "__main__":
    ingest_document()
    #sources = search("How do Kubernetes pods work?", top_k=5)
    query = input("Enter your question: ")
    search_results = search(query, top_k=20)

    context, sources = context_builder(query, top_k=5)
    #print(context)
    answer = generate_answer(
        query,
        context
    )

    print("\n===== ANSWER =====\n")
    print(answer)
    
    for source in sources:
        print(
            f"Page {source['page_number']} "
            f"| {source['document_id']}"
            f" | {source['distance']:.4f}"
            f" | {source['rerank_score']:.4f}"
        )

    
    
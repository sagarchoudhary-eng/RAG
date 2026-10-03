from sentence_transformers import CrossEncoder

model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")


def rerank(query, search_results, top_k=5):
    pairs = [
        (query, result["text"])
        for result in search_results
    ]

    scores = model.predict(pairs)

    ranked_results = []

    for result, score in zip(search_results, scores):
        result = result.copy()
        result["rerank_score"] = float(score)
        ranked_results.append(result)

    ranked_results.sort(
        key=lambda x: x["rerank_score"],
        reverse=True
    )

    return ranked_results[:top_k]
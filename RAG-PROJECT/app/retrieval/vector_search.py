import chromadb
# chunks = [
#     {
#         "id": "chunk_001",
#         "text": "Kubernetes pods are the smallest deployable units in Kubernetes. A pod can contain one or more containers.",
#         "metadata": {
#             "document_id": "doc_001",
#             "page": 1,
#             "department": "engineering"
#         }
#     },
#     {
#         "id": "chunk_002",
#         "text": "Kubernetes Services provide stable networking and expose applications running inside pods.",
#         "metadata": {
#             "document_id": "doc_001",
#             "page": 2,
#             "department": "engineering"
#         }
#     },
#     {
#         "id": "chunk_003",
#         "text": "Amazon S3 is an object storage service used to store files, backups, images, and other data.",
#         "metadata": {
#             "document_id": "doc_002",
#             "page": 1,
#             "department": "cloud"
#         }
#     }
# ]


client = chromadb.PersistentClient(path="./data/chroma")

collection = client.get_or_create_collection(
     name="doc_search"
 )

# collection.add(
#     ids=[chunk["id"] for chunk in chunks],
#     documents=[chunk["text"] for chunk in chunks],
#     metadatas=[chunk["metadata"] for chunk in chunks]
# )

results = collection.query(
     query_texts=["How do Kubernetes pods work?"],
     n_results=2
 )


print(results)
# # print("IDs:", results["ids"])
# # print("Documents:", results["documents"])
# # print("Metadata:", results["metadatas"])
# # print("Distances:", results["distances"])

# results = collection.query(
#     query_texts=["What is Amazon S3 used for?"],
#     n_results=2,
#     where={"department": "cloud"}
# )

# #print(results)

# #print(collection._embedding_function)

# result = collection.get(
#     ids=["chunk_001"],
#     include=["embeddings", "documents"]
# )

# print(result["documents"])
# print(len(result["embeddings"][0]))  # Print the embedding vector for chunk_001

# result = collection.get(
#     ids=["chunk_002"],
#     include=["embeddings"]
# )

# print(len(result["embeddings"][0]))


## chromadb retrival example

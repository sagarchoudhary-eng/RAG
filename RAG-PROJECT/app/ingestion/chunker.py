def chunk_text(pages,document_id):
    chunk_size = 1000
    chunk_overlap = 200

    if chunk_overlap >= chunk_size:
        raise ValueError("chunk_overlap must be smaller than chunk_size")

    chunks = []
    chunk_index = 0

    for page in pages:
        page_number = page["page_number"]
        text = page["text"]

        for i in range(0, len(text), chunk_size - chunk_overlap):
            chunk = text[i:i + chunk_size]

            chunks.append({
                "chunk_id": f"{document_id}_chunk_{chunk_index}",
                "document_id": document_id,
                "chunk_index": chunk_index,
                "page_number": page_number,
                "text": chunk
            })

            chunk_index += 1

    return chunks
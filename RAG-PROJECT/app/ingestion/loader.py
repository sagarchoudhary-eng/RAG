from pypdf import PdfReader
def load_document(path):
    """
    Load a document from the specified path and return its content as a string.
    """
    reader = PdfReader(path)
    pages = []
    for page_number,page in enumerate(reader.pages):
        text = page.extract_text()
        if text:
            pages.append({
                        "page_number": page_number,
                        "text": text
                    })
    return pages  
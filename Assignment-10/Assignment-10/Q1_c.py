"""code-aware chunking"""
from langchain_text_splitters import RecursiveCharacterTextSplitter
code_text = """
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b
"""
code_splitter = RecursiveCharacterTextSplitter.from_language(
    language="python",
    chunk_size=30,
    chunk_overlap=20
)
docs = code_splitter.create_documents([code_text])
for i, doc in enumerate(docs):
    print(f"Chunk {i+1}:")
    print(doc.page_content)
  

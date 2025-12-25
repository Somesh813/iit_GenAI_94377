"""Basic fixed-size chunking"""
from langchain_text_splitters import CharacterTextSplitter

raw_text = """
LangChain is a framework for developing applications powered by language models.
It enables data-aware and agentic applications.
"""

text_splitter = CharacterTextSplitter(
    separator="",chunk_size=30,chunk_overlap=20
)

docs = text_splitter.create_documents([raw_text])

for i, doc in enumerate(docs):
    print(f"Chunk {i+1}: {doc.page_content}")

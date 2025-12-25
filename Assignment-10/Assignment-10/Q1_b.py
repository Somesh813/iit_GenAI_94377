"""Recursive Character chunking"""
from langchain_text_splitters import RecursiveCharacterTextSplitter

raw_text = """
LangChain is a framework for developing applications powered by language models.
It enables data-aware and agentic applications.
"""

text_splitter=RecursiveCharacterTextSplitter(separators=["\n\n","\n","",""],chunk_size=30,chunk_overlap=20)
docs=text_splitter.create_documents([raw_text])


print(docs)
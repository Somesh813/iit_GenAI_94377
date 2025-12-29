import os
import streamlit as st
import chromadb
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain.chat_models import init_chat_model

st.set_page_config(page_title="AI Resume Handler", layout="wide")
st.title("🧠 AI Resume Handler (Agentic RAG)")

RESUME_DIR = "./resumes"
CHROMA_DIR = "./chroma_db"

if not os.path.exists(RESUME_DIR):
    st.error("❌ 'resumes' directory not found. Please add resume PDFs.")
    st.stop()

embed_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

client = chromadb.Client(
    settings=chromadb.Settings(persist_directory=CHROMA_DIR)
)
collection = client.get_or_create_collection(name="resume_collection")
if collection.count() == 0:
    st.info("📄 Indexing resumes for the first time...")

    loader = DirectoryLoader(
        path=RESUME_DIR,
        glob="**/*.pdf",
        loader_cls=PyPDFLoader
    )

    documents = loader.load()

    for doc in documents:
        doc.metadata["pdf_name"] = os.path.basename(doc.metadata["source"])
        doc.metadata["page_number"] = doc.metadata["page"] + 1

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=50,
        separators=["\n\n", "\n", " "]
    )

    chunks = splitter.split_documents(documents)
    texts = []
    metadatas = []
    ids = []

    for idx, chunk in enumerate(chunks):
        texts.append(chunk.page_content)
        chunk.metadata["chunk_id"] = str(idx)
        chunk.metadata["chunk_size"] = len(chunk.page_content)
        metadatas.append(chunk.metadata)
        ids.append(str(idx))

    embeddings = embed_model.embed_documents(texts)

    collection.add(
        ids=ids,
        documents=texts,
        embeddings=embeddings,
        metadatas=metadatas
    )

    st.success("✅ Resumes indexed successfully!")

else:
    st.success("✅ Resumes already indexed")

query = st.chat_input("🔍 Enter your query (e.g., Python developer, ML engineer, Fresher)...")

if query:
    # Vector search
    query_embedding = embed_model.embed_query(query)
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )

    st.subheader("📄 Retrieved Resume Chunks")

    for doc, meta in zip(results["documents"][0], results["metadatas"][0]):
        st.markdown(f"**📁 File:** {meta['pdf_name']} | **📄 Page:** {meta['page_number']}")
        st.write(doc[:300] + "...")
        st.markdown("---")
        
    llm = init_chat_model(
        model="microsoft/phi-4",
        model_provider="openai",
        base_url="http://127.0.0.1:1234/v1",
        api_key="not-needed"
    )

    llm_prompt = f"""
User Query:
{query}

Resume Context:
{results["documents"][0]}

Instruction:
- Identify best candidate matching the query
- Extract names and key skills only
- Do NOT add explanations
- Do NOT add extra text
- Return original resume content only
"""

    response = llm.invoke(llm_prompt)

    st.subheader("🎯 AI Result")
    st.write(response.content)

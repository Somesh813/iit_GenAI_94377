import os
import chromadb
import streamlit as st
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain.chat_models import init_chat_model

st.set_page_config(page_title="AI Resume Handler", layout="wide")
st.title("AI Resume Handler")

RESUME_DIR="resumes"
DB_DIR="./chroma_db"

os.makedirs(RESUME_DIR, exist_ok=True)

embed_model=HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

client=chromadb.Client(
    settings=chromadb.Settings(persist_directory=DB_DIR)
)
collection=client.get_or_create_collection(name="resume_collection")

menu=st.sidebar.selectbox(
    "Select Option",
    ["Upload Resumes", "List Resumes", "Delete Resume", "Search Resumes"]
)

if menu=="Upload Resumes":
    st.header("Upload Multiple Resume PDFs")

    files=st.file_uploader(
        "Upload Resume PDFs",
        type="pdf",
        accept_multiple_files=True
    )

    if st.button("Process & Store Resumes"):
        if not files:
            st.warning("Please upload at least one resume.")
        else:
            texts, metadatas, ids = [], [], []
            splitter=RecursiveCharacterTextSplitter(
                chunk_size=800,
                chunk_overlap=50
            )

            doc_id=collection.count()

            for file in files:
                save_path=os.path.join(RESUME_DIR, file.name)

                with open(save_path, "wb") as f:
                    f.write(file.getbuffer())

                loader=PyPDFLoader(save_path)
                documents=loader.load()
                chunks=splitter.split_documents(documents)

                for chunk in chunks:
                    texts.append(chunk.page_content)
                    metadatas.append({
                        "pdf_name": file.name,
                        "page_number": chunk.metadata.get("page", 0) + 1
                    })
                    ids.append(str(doc_id))
                    doc_id += 1

            embeddings = embed_model.embed_documents(texts)
            collection.add(
                ids=ids,
                documents=texts,
                embeddings=embeddings,
                metadatas=metadatas
            )

            st.success(f"{len(files)} resumes uploaded successfully!")

elif menu == "List Resumes":
    st.header("Uploaded Resumes")
    files = os.listdir(RESUME_DIR)

    if files:
        for f in files:
            st.write("📄", f)
    else:
        st.info("No resumes uploaded.")

elif menu == "Delete Resume":
    st.header("Delete Resume")

    files = os.listdir(RESUME_DIR)
    selected = st.selectbox("Select Resume", files)

    if st.button("Delete"):
        collection.delete(where={"pdf_name": selected})
        os.remove(os.path.join(RESUME_DIR, selected))
        st.success("Resume deleted successfully!")

elif menu == "Search Resumes":
    st.header("Search Resumes")

    query = st.chat_input("Enter your query regarding resumes")

    if query:
        query_embedding = embed_model.embed_query(query)

        # Get more chunks first
        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=10
        )

        # One chunk per resume
        unique_docs = []
        seen_resumes = set()

        for doc, meta in zip(
            results["documents"][0],
            results["metadatas"][0]
        ):
            if meta["pdf_name"] not in seen_resumes:
                unique_docs.append(doc)
                seen_resumes.add(meta["pdf_name"])

            if len(unique_docs) == 3:
                break

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
{unique_docs}

Instruction:
- Identify the best matching candidates
- Use only resume content
- No extra explanation
- Give original content only
"""

        response = llm.invoke(llm_prompt)

        st.subheader("AI Analysis Result")
        st.write(response.content)

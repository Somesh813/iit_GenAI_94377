from langchain_openai import OpenAIEmbeddings

embed_model = OpenAIEmbeddings(
    model="nomic-embed-text-v1.5",
    base_url="http://127.0.0.1:1234/v1",
    api_key="not-needed"
)

sentences = [
    "I like Artificial Intelligence",
    "Generative AI is magnificent",
    "World is amazing"
]

embeddings = embed_model.embed_documents(sentences)

for embedding in embeddings:
    print(f"Len = {len(embedding)} --> {embedding[:4]}")

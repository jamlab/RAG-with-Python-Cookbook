import os
from pathlib import Path
import chromadb
from openai import OpenAI
from dotenv import load_dotenv

import httpx
from chromadb.config import Settings

#region --- Functions ---
def chunk_text(text, size=1000, overlap=200):
    chunks, start = [], 0
    while start < len(text):
        end = min(start + size, len(text))  # end of chunk
        if end < len(text):
            bp = text.rfind("\n\n", start, end)
            if bp == -1:
                bp = text.rfind(". ", start, end)
            if bp > start:
                end = bp + 1
        chunk = text[start:end].strip()
        if chunk:
            chunks.append(chunk)
        start = end - overlap if end < len(text) else end
    return chunks

def embed_and_store(chunks, db_path, collection_name, client, embedding_model="text-embedding-3-small"):
    chroma = chromadb.PersistentClient(path=str(db_path),
                                       settings=Settings(anonymized_telemetry=False),)
    collection = chroma.get_or_create_collection(
        name=collection_name,
        metadata={"description": "Harry Potter knowledge base"},
    )
    if collection.count() > 0:
        return collection

    # collection does not exist, create it
    embeddings = []
    for i in range(0, len(chunks), 100):
        batch = chunks[i : i + 100]
        res = client.embeddings.create(model=embedding_model, input=batch)
        embeddings.extend([x.embedding for x in res.data])

    collection.add(
        ids=[f"chunk_{i}" for i in range(len(chunks))],
        documents=chunks,
        embeddings=embeddings,
        metadatas=[{"chunk_index": i} for i in range(len(chunks))],
    ) #
    return collection

def retrieve(question, collection, client, embedding_model="text-embedding-3-small", top_k=3):
    q_emb = client.embeddings.create(
        model=embedding_model,
        input=question,
    ).data[0].embedding

    res = collection.query(
        query_embeddings=[q_emb],
        n_results=top_k,
        include=["documents"],
    )

    return res["documents"][0]

def answer(question, docs, client):
    context = "\n\n---\n\n".join(docs)
    prompt = f"""Answer the question using only the context below.

Context:
{context}

Question:
{question}

Answer:"""

    res = client.chat.completions.create(
        model=os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT"),
        messages=[{"role": "user", "content": prompt}],
    )

    return res.choices[0].message.content

#endregion --- Functions ---

def main():
    # Load text file
    base_datasets_dir = Path("../datasets")
    file_path = base_datasets_dir / "text_files" / "harry_potter_knowledge_base.txt"
    if not file_path.exists():
        file_path = Path("./datasets/text_files/harry_potter_knowledge_base.txt")

    text = file_path.read_text(encoding="utf-8")

    # Chunk text
    chunks = chunk_text(text)

    load_dotenv(override=True)
    client = OpenAI(
        api_key=os.getenv("AZURE_OPENAI_KEY"),
        base_url=os.getenv("AZURE_OPENAI_ENDPOINT"),
        http_client=httpx.Client(),
    )

    # Emnbed and store chunks
    # Create a new chroma database with embeddings out of the chunks
    chroma_db_dir = Path("chroma_db")
    collection = embed_and_store(chunks, chroma_db_dir, "harry_potter_kb", os.getenv("AZURE_OPENAI_EMBEDDING_MODEL"))

    question = "Why did Uncle Vernon take the family to a hut in the middle of the sea?"
    docs = retrieve(question, client=client, collection=collection )
    answer_text = answer(question, docs, client)
    print(f"Question: {question}")
    print(answer_text)

if __name__ == '__main__':
    main()


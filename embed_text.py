from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
import os
import shutil


def embed_docs(chunks: list, chroma_path: str):
    embedding_model = OllamaEmbeddings(model="mistral:instruct")

    # Erase Existing Chroma DB and Persist new one
    if os.path.exists(chroma_path):
            shutil.rmtree(chroma_path)


    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=chroma_path
    )
    print(f"{len(chunks)} chunks saved to {chroma_path}.")
    return vector_store
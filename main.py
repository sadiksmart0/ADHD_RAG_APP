#--------External Packages---------#
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import OllamaLLM

import os
import shutil
from dotenv import load_dotenv
load_dotenv()
MISTRAL_API_KEY= os.getenv("MISTRAL_API_KEY")
#--------Internal Packages---------#
from load_data import load_pdf
from split_text import split_text
from embed_text import embed_docs

#--------- PATHS -------------------#
CHROMA_PATH = "/Users/abubakarmuktar/Documents/RAG_Projects/ADHD_RAG_APP/Chroma_DB"
DATA_PATH = "/Users/abubakarmuktar/Documents/RAG_Projects/ADHD_RAG_APP/Data"

SWITCH = False

#----Setting prompt Template--------#
prompt = ChatPromptTemplate.from_template("""
Answer the question based only on the following context and 
write out the context as well:

{context}

---

Answer the question based on the above context: {question}

""")

model = OllamaLLM(
    model="mistral:instruct",
    temperature=0.7
)


def main():
    # Embed the documents only once
    print("-------STARTED LOADING FILE---------\n")
    loaded_docs = load_pdf(DATA_PATH)
    print("-------DONE LOADING FILE------------\n")

    print("-------STARTED SPLITTING TEXT---------\n")
    chunks = split_text(loaded_docs)
    print("-------DONE SPLITTING TEXT-----------\n")

    print("----STARTED EMBEDDING AND STORING----\n")
    vector_store = embed_docs(chunks, CHROMA_PATH)
    print("-------DONE EMBEDDING TEXT-----------\n")

    # Start the retrieval and query loop
    retriever = retrieve(vector_store)

    while True:
        # Ask the user if they want to query or exit
        user_input = input("\nType 'query' to ask a question or 'exit' to quit the program: ").strip().lower()

        if user_input == "exit":
            print("Exiting the program. Goodbye!")
            break
        elif user_input == "query":
            print("-------STARTED RETRIEVING------------\n")
            result = query(retriever)
            print(f"\n\n-------RESULT-------\n\n{result}")
        else:
            print("Invalid input. Please type 'query' or 'exit'.")



def retrieve(db):
    retriever = db.as_retriever(
    search_type="similarity",
    search_kwargs={"k":5}
    )
    return retriever


def query(retriever):

    # Chaining input and output
    chain = (
    {"context":retriever, "question":RunnablePassthrough()}
    | prompt
    | model
    | StrOutputParser()
    )
    question = str(input("\nPLEASE TYPE IN YOUR QUESTION BASED ON THE DOCUMENT TOPIC:\n"))
    return chain.invoke(question)
    
if __name__ == "__main__":
        main()


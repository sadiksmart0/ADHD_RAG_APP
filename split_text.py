from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_text(documents: list) -> list:
    doc_splitter = RecursiveCharacterTextSplitter(
                separators=["\n\n", "\n", "."],
                chunk_size=1000,
                chunk_overlap=0,
                length_function=len,
                is_separator_regex=False
                )
    
    return doc_splitter.split_documents(documents)
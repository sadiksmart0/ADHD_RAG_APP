from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders import PyPDFLoader




def load_pdf(path: str) -> list:
    doc_loader = DirectoryLoader(
        path=path, 
        glob="*.pdf",
        show_progress=True,
        loader_cls=PyPDFLoader
        )
    loaded = doc_loader.load()
    print(f"Loaded {len(loaded)} document into Memory")

    return loaded
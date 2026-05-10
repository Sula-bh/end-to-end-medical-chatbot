from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter


def load_pdf(data):
    loader = PyPDFDirectoryLoader(data)
    documents = loader.load()
    return documents


def split_text(data):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=20)
    text_chunks = text_splitter.split_documents(data)
    return text_chunks


def download_embedding_model():
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
    model_kwargs = {"device": "cpu"}

    embeddings = HuggingFaceEmbeddings(model_name=model_name, model_kwargs=model_kwargs)

    return embeddings

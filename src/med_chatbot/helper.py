from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

from med_chatbot.logger import logging


def load_pdf(data):
    logging.info("Loading PDF files from directory")

    loader = PyPDFDirectoryLoader(data)
    documents = loader.load()

    logging.info(f"Successfully loaded {len(documents)} documents")

    return documents


def split_text(data):
    logging.info("Splitting documents into chunks")

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=700, chunk_overlap=100)
    text_chunks = text_splitter.split_documents(data)

    logging.info(f"Created {len(text_chunks)} text chunks")

    return text_chunks


def download_embedding_model():
    logging.info("Downloading embedding model")

    model_name = "BAAI/bge-base-en-v1.5"
    model_kwargs = {"device": "cpu"}

    embeddings = HuggingFaceEmbeddings(model_name=model_name, model_kwargs=model_kwargs)

    logging.info("Embedding model loaded successfully")

    return embeddings

import os

from dotenv import load_dotenv
from langchain_pinecone import PineconeVectorStore

from med_chatbot.helper import download_embedding_model, load_pdf, split_text
from med_chatbot.logger import logging

logging.info("Loading environment variables")

load_dotenv()

INDEX_NAME = os.getenv("PINECONE_INDEX_NAME")

logging.info(f"Pinecone index name loaded: {INDEX_NAME}")


logging.info("Starting PDF ingestion pipeline")

data_path = os.path.join(os.getcwd(), "data")

logging.info(f"Loading data from: {data_path}")

extracted_data = load_pdf(data_path)

logging.info("PDF loading completed")


logging.info("Starting text splitting process")

text_chunks = split_text(extracted_data)

logging.info(f"Text splitting completed with {len(text_chunks)} chunks")


logging.info("Loading embedding model")

embeddings = download_embedding_model()

logging.info("Embedding model loaded successfully")


logging.info("Starting Pinecone vector store upload")

docsearch = PineconeVectorStore.from_texts(
    texts=[t.page_content for t in text_chunks],
    embedding=embeddings,
    index_name=INDEX_NAME,
)

logging.info("Vector embeddings successfully stored in Pinecone")

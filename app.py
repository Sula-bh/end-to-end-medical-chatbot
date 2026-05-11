import os

from dotenv import load_dotenv
from flask import Flask, Response, render_template, request
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_ollama import ChatOllama
from langchain_pinecone import PineconeVectorStore

from med_chatbot.helper import download_embedding_model
from med_chatbot.logger import logging
from med_chatbot.prompt import prompt_template

logging.info("Loading environment variables")

load_dotenv()

app = Flask(__name__)

logging.info("Downloading embedding model")

embeddings = download_embedding_model()

INDEX_NAME = os.getenv("PINECONE_INDEX_NAME")

logging.info(f"Pinecone index loaded: {INDEX_NAME}")

logging.info("Connecting to Pinecone vector store")

docsearch = PineconeVectorStore(index_name=INDEX_NAME, embedding=embeddings)

prompt = ChatPromptTemplate.from_template(prompt_template)

logging.info("Initializing Ollama model")

llm = ChatOllama(model="llama3.2:3b", temperature=0.8, num_predict=512, streaming=True)

retriever = docsearch.as_retriever(search_kwargs={"k": 3})

logging.info("Creating RAG chain")

chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)


@app.route("/")
def index():
    logging.info("Rendering chat UI")
    return render_template("chat.html")


@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]

    logging.info(f"User query received: {msg}")

    def generate():
        logging.info("Starting streamed response generation")

        for chunk in chain.stream(msg):
            yield chunk

        logging.info("Streaming completed")

    return Response(generate(), mimetype="text/plain")


if __name__ == "__main__":
    logging.info("Starting Flask application")

    app.run(host="0.0.0.0", port=8080, debug=True)

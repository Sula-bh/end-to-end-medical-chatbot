import os

from dotenv import load_dotenv
from flask import Flask, Response, render_template, request
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_ollama import ChatOllama
from langchain_pinecone import PineconeVectorStore

from med_chatbot.helper import download_embedding_model
from med_chatbot.prompt import prompt_template

load_dotenv()

app = Flask(__name__)

embeddings = download_embedding_model()

INDEX_NAME = os.getenv("PINECONE_INDEX_NAME")

docsearch = PineconeVectorStore(index_name=INDEX_NAME, embedding=embeddings)

prompt = ChatPromptTemplate.from_template(prompt_template)

llm = ChatOllama(model="llama3.2:3b", temperature=0.8, num_predict=512, streaming=True)

retriever = docsearch.as_retriever(search_kwargs={"k": 3})

chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)


@app.route("/")
def index():
    return render_template("chat.html")


@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]

    def generate():
        for chunk in chain.stream(msg):
            yield chunk

    return Response(generate(), mimetype="text/plain")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)

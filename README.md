# 🩺 End-to-End Medical RAG Chatbot

An AI-powered Medical Chatbot built using Retrieval-Augmented Generation (RAG) with Flask, Pinecone, LangChain, and Ollama.

The chatbot retrieves relevant medical information from the Gale Encyclopedia of Medicine and generates context-aware responses using a local LLM.

---

# 🚀 Features

- 🔍 Retrieval-Augmented Generation (RAG)
- 📚 Medical knowledge retrieval from PDF documents
- 🧠 Semantic search using Pinecone Vector Database
- 🤖 Local LLM inference using Ollama
- ⚡ Real-time streaming responses
- 💬 Interactive chatbot UI with Flask + Bootstrap
- 📄 PDF ingestion and intelligent text chunking
- 📝 Logging support for debugging and monitoring
- 🎨 Modern responsive chat interface
- 🔒 Input sanitization against HTML injection

---

# 🛠️ Tech Stack

## Backend
- Python
- Flask
- LangChain
- Pinecone
- Ollama

## Frontend
- HTML
- CSS
- Bootstrap
- JavaScript
- jQuery

## Embedding Model
- BAAI/bge-small-en-v1.5

## LLM
- Llama 3.2 3B (via Ollama)

---

# 📂 Project Structure

```text
medical-rag-chatbot/
│
├── src/
│   └── med_chatbot/
│       ├── __init__.py
│       ├── helper.py
│       ├── logger.py
│       └── prompt.py
│
├── data/
├── logs/
├── notebooks/
├── static/
│   ├── css/
│   └── images/
│
├── templates/
│   └── chat.html
│
├── app.py
├── store_index.py
├── requirements.txt
├── setup.py
├── README.md
└── .env
```

---

# ⚙️ Installation

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/Sula-bh/end-to-end-medical-chatbot.git

cd end-to-end-medical-chatbot
```

---


## 2️⃣ Create Conda Environment

```bash
conda create -n medbot python=3.13

conda activate medbot
```


## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the root directory.

```env
PINECONE_API_KEY=your_pinecone_api_key
PINECONE_INDEX_NAME=your_index_name
```

---

# 🤖 Install Ollama

Download and install Ollama:

https://ollama.com

Pull the required model:

```bash
ollama pull llama3.2:3b
```

Run Ollama locally:

```bash
ollama serve
```

---

# 📚 Add Medical PDFs

Place your medical PDF files inside the `data/` folder.

Example:

```text
data/
└── Gale_Encyclopedia_of_Medicine.pdf
```

---

# 🧠 Create Vector Embeddings

Run:

```bash
python store_index.py
```

This will:
- Load PDFs
- Split text into chunks
- Generate embeddings
- Store vectors in Pinecone

---

# ▶️ Run the Application

```bash
python app.py
```

Open in browser:

```text
http://localhost:8080
```

---

# 💬 Example Questions

- What is paracetamol?
- What causes cancer?
- What are the symptoms of diabetes?
- What is hypertension?
- Explain osteoarthritis.

---

# 🔄 Streaming Responses

The chatbot supports:
- real-time token streaming
- typing indicator animation
- auto-scroll chat updates

---

# 📸 UI Features

- Responsive chatbot layout
- Animated typing indicator
- Styled scrollbar
- Chat history persistence during session
- Medical-themed interface

---

# 📝 Logging

Logs are automatically stored inside:

```text
logs/
```

Includes:
- PDF loading logs
- embedding generation logs
- retrieval logs
- user query logs
- streaming logs

---

# 🔒 Security Features

- HTML input sanitization
- Safer text rendering
- Prevention against basic XSS injection

---

# 👨‍💻 Author

Sulabh Acharya

GitHub: https://github.com/Sula-bh
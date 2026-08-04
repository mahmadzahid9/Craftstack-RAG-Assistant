# CraftStack RAG Assistant

A modern **Retrieval-Augmented Generation (RAG)** chatbot built with **Flask** that allows users to upload PDF documents and ask intelligent questions based on their contents using Large Language Models (LLMs).

---

## Features

- 📄 PDF document upload
- 🧠 Retrieval-Augmented Generation (RAG)
- 🔍 Semantic search using vector embeddings
- 🤖 AI-powered question answering
- 💬 Modern ChatGPT-inspired user interface
- ⚡ Fast Flask backend
- 🎨 Responsive glassmorphism design
<<<<<<< HEAD
- 🌐 Live internet search integration (DuckDuckGo)
- 🪙 Live market rates integration (Gold price and Exchange Rates)
=======
>>>>>>> 4d52048358528884a01ac7ce28c94f927d0fdd3d

---

## Tech Stack

### Backend
<<<<<<< HEAD
- Flask (Web Server)
- ChromaDB (Vector Database)
- Sentence Transformers (Embedding Generation)
- Hugging Face Inference API (LLM Orchestration)
- PyPDF (PDF Parsing)
- DuckDuckGo Search (Web Search API)
- Requests
=======
- Flask
- LangChain
- ChromaDB
- Sentence Transformers
- Hugging Face Inference API
>>>>>>> 4d52048358528884a01ac7ce28c94f927d0fdd3d

### Frontend
- HTML
- Tailwind CSS
- JavaScript
- GSAP Animations

---

## Project Structure

```text
CraftStack-RAG-Assistant/
│
├── app.py
<<<<<<< HEAD
├── ingest.py
├── rag.py
├── search.py
├── tools.py
├── requirements.txt
├── .env
├── templates/
│   └── index.html
├── static/
│   ├── script.js
│   └── style.css
├── documents/
├── vector_db/
=======
├── requirements.txt
├── .env
├── templates/
├── static/
├── uploads/
├── vectordb/
>>>>>>> 4d52048358528884a01ac7ce28c94f927d0fdd3d
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/mahmadzahid9/Craftstack-RAG-Assistant.git
cd Craftstack-RAG-Assistant
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
HF_TOKEN=your_huggingface_token
```

Run the application:

```bash
python app.py
```

Open:

```
http://127.0.0.1:5000
```

---

## Usage

1. Launch the application.
<<<<<<< HEAD
2. Upload a PDF document using the "+" button or header button.
=======
2. Upload a PDF document.
>>>>>>> 4d52048358528884a01ac7ce28c94f927d0fdd3d
3. Wait for indexing to complete.
4. Ask questions related to the uploaded document.
5. The assistant retrieves relevant context and generates accurate responses.

---

## Future Improvements

- Multi-document support
- Conversation memory
- Streaming responses
- OCR for scanned PDFs
- User authentication
- Chat history
- Citation support
- Multiple vector database options

---

## Author

**Muhammad Ahmed**

Built as a learning project to explore Retrieval-Augmented Generation (RAG), vector databases, semantic search, and Large Language Models.

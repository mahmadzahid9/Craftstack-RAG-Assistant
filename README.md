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
- 🌐 Live internet search integration (DuckDuckGo)
- 🪙 Live market rates integration (Gold Price & Exchange Rates)

---

## Tech Stack

### Backend

- Flask (Web Server)
- ChromaDB (Vector Database)
- Sentence Transformers (Embedding Generation)
- Hugging Face Inference API (LLM)
- PyPDF (PDF Parsing)
- DuckDuckGo Search
- Requests

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
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/mahmadzahid9/Craftstack-RAG-Assistant.git
cd Craftstack-RAG-Assistant
```

Install the required dependencies:

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

Open your browser and navigate to:

```text
http://127.0.0.1:5000
```

---

## Usage

1. Launch the application.
2. Upload a PDF document using the upload button.
3. Wait for the document to be indexed.
4. Ask questions related to the uploaded PDF.
5. Use live web search for up-to-date information when needed.
6. Retrieve live Gold Prices and Exchange Rates through integrated tools.

---

## Future Improvements

- Multi-document support
- Conversation memory
- Streaming responses
- OCR support for scanned PDFs
- User authentication
- Chat history
- Source citations
- Multiple vector database options
- Multi-file document retrieval
- Drag-and-drop PDF uploads

---

## Author

**Muhammad Ahmed**

Built as a learning project to explore Retrieval-Augmented Generation (RAG), vector databases, semantic search, live tool integration, and Large Language Models.

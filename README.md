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

---

## Tech Stack

### Backend
- Flask
- LangChain
- ChromaDB
- Sentence Transformers
- Hugging Face Inference API

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
├── requirements.txt
├── .env
├── templates/
├── static/
├── uploads/
├── vectordb/
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
2. Upload a PDF document.
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

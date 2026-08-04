import os
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
import chromadb

DOCUMENTS_DIR = "documents"
VECTOR_DB_DIR = "vector_db"

# Load embedding model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# Connect to ChromaDB
client = chromadb.PersistentClient(path=VECTOR_DB_DIR)

collection = client.get_or_create_collection(
    name="documents"
)


# ----------------------------
# Read PDF
# ----------------------------

def read_pdf(file_path):

    reader = PdfReader(file_path)

    text = ""

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


# ----------------------------
# Chunk Text
# ----------------------------

def chunk_text(text, chunk_size=500):

    return [
        text[i:i + chunk_size]
        for i in range(0, len(text), chunk_size)
    ]


# ----------------------------
# Index ONE PDF
# ----------------------------

def ingest_pdf(file_path):

    pdf_name = os.path.basename(file_path)

    print(f"\n=== [STAGES 1-4] Ingesting PDF: {pdf_name} ===")

    # Stage 1: PDF Text Extraction
    text = read_pdf(file_path)
    text_length = len(text)
    print(f"[Stage 1: PDF Extraction] Extracted text length: {text_length} characters")
    if text_length > 0:
        print(f"[Stage 1: PDF Extraction] Sample text (first 300 chars):\n{text[:300]}")
    else:
        print("[Stage 1: PDF Extraction] WARNING: Extracted text is empty! This might be an image/scanned PDF without OCR.")

    # Stage 2: Text Chunking
    chunks = chunk_text(text)
    print(f"[Stage 2: Text Chunking] Created {len(chunks)} chunks")
    if len(chunks) > 0:
        avg_chunk_size = sum(len(c) for c in chunks) / len(chunks)
        print(f"[Stage 2: Text Chunking] Average chunk size: {avg_chunk_size:.2f} characters")
        print(f"[Stage 2: Text Chunking] Sample chunk 1:\n{chunks[0][:200]}...")
    else:
        print("[Stage 2: Text Chunking] No chunks created (empty text).")

    # Stage 3: Embedding Generation
    if len(chunks) > 0:
        print("[Stage 3: Embedding Generation] Starting embedding generation...")
        try:
            embeddings = embedding_model.encode(chunks)
            print(f"[Stage 3: Embedding Generation] Generated {len(embeddings)} embeddings of shape {embeddings.shape}")
        except Exception as e:
            print(f"[Stage 3: Embedding Generation] ERROR: Embedding generation failed: {e}")
            raise e
    else:
        embeddings = []

    # Stage 4: Vector Database Insertion
    if len(chunks) > 0:
        print("[Stage 4: Vector DB] Inserting chunks into collection 'documents'...")
        try:
            for i, (chunk, embedding) in enumerate(zip(chunks, embeddings)):
                collection.add(
                    ids=[f"{pdf_name}_{i}"],
                    documents=[chunk],
                    embeddings=[embedding.tolist()],
                    metadatas=[
                        {
                            "source": pdf_name
                        }
                    ]
                )
            print(f"[Stage 4: Vector DB] Successfully inserted {len(chunks)} chunks.")
            total_docs = collection.count()
            print(f"[Stage 4: Vector DB] Total indexed documents in 'documents' collection: {total_docs}")
        except Exception as e:
            print(f"[Stage 4: Vector DB] ERROR: Failed to insert into Vector DB: {e}")
            raise e
    else:
        print("[Stage 4: Vector DB] Skipping database insertion (0 chunks).")

    print("=== Ingestion Finished ===\n")


# ----------------------------
# Index ALL PDFs
# ----------------------------

def ingest():

    pdf_files = [
        f for f in os.listdir(DOCUMENTS_DIR)
        if f.endswith(".pdf")
    ]

    print(f"\nFound {len(pdf_files)} PDF(s).\n")

    for pdf in pdf_files:

        ingest_pdf(
            os.path.join(DOCUMENTS_DIR, pdf)
        )


if __name__ == "__main__":
    ingest()
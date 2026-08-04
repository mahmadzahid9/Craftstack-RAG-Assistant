from ingest import ingest_pdf
from tools import get_gold_price
from search import web_search
from rag import retrieve, retrieve_with_relevance

from flask import Flask, render_template, request, jsonify
from huggingface_hub import InferenceClient
from dotenv import load_dotenv
from werkzeug.utils import secure_filename

import shutil
import os

LIVE_KEYWORDS = [
    "today",
    "latest",
    "current",
    "weather",
    "gold",
    "bitcoin",
    "stock",
    "price",
    "news",
    "live",
    "score",
    "who won",
    "temperature"
]

app = Flask(__name__)

# ==========================
# Hugging Face Setup
# ==========================

load_dotenv(override=True)

HF_TOKEN = os.getenv("HF_TOKEN")

if not HF_TOKEN:
    raise ValueError("HF_TOKEN not found in .env file")

client = InferenceClient(
    token=HF_TOKEN
)

@app.route("/")
def home():
    return render_template("index.html")

# ==========================
# Upload PDF
# ==========================

@app.route("/upload", methods=["POST"])
def upload_pdf():

    file = request.files["pdf"]

    if file.filename == "":
        return jsonify({
            "message": "No file selected."
        })

    filename = secure_filename(file.filename)

    path = os.path.join("documents", filename)

    file.save(path)

    # Automatically index the uploaded PDF
    ingest_pdf(path)

    return jsonify({
        "message": f"{filename} uploaded and indexed successfully."
    })

# ==========================
# Chat
# ==========================

@app.route("/chat", methods=["POST"])
def chat():

    try:

        data = request.get_json()
        message = data["message"]

        print(f"\nUser: {message}")

        # ==========================
        # Gold Questions
        # ==========================

        if "gold" in message.lower():

            print("\nFetching Gold API...\n")

            live_data = get_gold_price()

            print("=" * 80)
            print("GOLD API DATA")
            print("=" * 80)
            print(live_data)
            print("=" * 80)

            messages = [
                {
                    "role": "system",
                    "content": f"""
You are CraftStack AI.

The following contains LIVE gold market data.

If the user asks for the gold price in Pakistan:

- Use the USD to PKR exchange rate provided.
- 1 troy ounce = 31.1035 grams.
- 1 tola = 11.6638 grams.
- Calculate the price yourself.
- Give the answer in PKR.
- Mention it is an estimated value.

If the user asks for the international gold price, answer directly.

Live Data:

{live_data}
"""
                },
                {
                    "role": "user",
                    "content": message
                }
            ]

        # ==========================
        # Live Internet Questions
        # ==========================

        elif any(keyword in message.lower() for keyword in LIVE_KEYWORDS):

            print("\nSearching DuckDuckGo...\n")

            internet_info = web_search(message)

            print("=" * 80)
            print("SEARCH RESULTS")
            print("=" * 80)
            print(internet_info)
            print("=" * 80)

            messages = [
                {
                    "role": "system",
                    "content": f"""
You are CraftStack AI.

The following information was retrieved from the internet.

Answer ONLY using this information.

If prices or values are present, include them.

Do NOT say:
- I don't have access to live data.
- I couldn't find the information.

Unless the search results are empty.

Internet Search Results:

{internet_info}
"""
                },
                {
                    "role": "user",
                    "content": message
                }
            ]

        # ==========================
        # RAG / Normal Conversation
        # ==========================

        else:
            print(f"\n--- [Stage 7: Chat Flow Trace] Tracing request: '{message}' ---")
            
            # Check DB relevance
            is_relevant, context = retrieve_with_relevance(message)
            
            is_keyword_match = any(word in message.lower() for word in [
                "leave",
                "policy",
                "insurance",
                "attendance",
                "employee",
                "company",
                "working hours",
                "handbook"
            ])

            if is_relevant or is_keyword_match:
                print(f"[Stage 7: Chat Flow Trace] Routing to RAG Pipeline (is_relevant={is_relevant}, is_keyword_match={is_keyword_match})")
                
                # Fetch context if we skipped it during check or if we need a refresh
                if not context:
                    print("[Stage 7: Chat Flow Trace] Fetching context due to keyword match fallback...")
                    context = retrieve(message)
                
                # Stage 6: Prompt Construction
                print("\n=== [Stage 6: Prompt Construction] Preparing RAG Prompt ===")
                system_content = f"""
You are CraftStack AI.

Answer ONLY using the following context.

If the answer cannot be found in the context, reply exactly:

I couldn't find that information in the uploaded documents.

Context:

{context}
"""
                print(f"[Stage 6: Prompt Construction] System prompt structure details:")
                print(f"  - Context length: {len(context)} characters")
                print(f"  - Contains context? {'Yes' if context else 'No'}")
                print(f"  - Instructions present? Yes (Strict 'Answer ONLY using the following context')")
                
                messages = [
                    {
                        "role": "system",
                        "content": system_content
                    },
                    {
                        "role": "user",
                        "content": message
                    }
                ]
                
                print("[Stage 7: Chat Flow Trace] Prompt ready. Sending to LLM.")
            else:
                print("[Stage 7: Chat Flow Trace] Routing to Normal Conversation (No relevant database document found).")
                messages = [
                    {
                        "role": "user",
                        "content": message
                    }
                ]

        print("\nCalling Hugging Face...\n")

        completion = client.chat.completions.create(
            model="Qwen/Qwen2.5-7B-Instruct",
            messages=messages,
            max_tokens=512,
            temperature=0.7
        )

        response = completion.choices[0].message.content

        print("\nBot:", response)

        return jsonify({
            "response": response
        })

    except Exception as e:

        print("\nERROR:", e)

        return jsonify({
            "response": str(e)
        })


if __name__ == "__main__":
    app.run(debug=False)
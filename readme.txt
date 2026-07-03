Stripe Documentation Assistant using RAG and Unsloth

Overview

This project is a Retrieval-Augmented Generation (RAG) based chatbot that answers questions related to Stripe documentation. The system retrieves relevant information from Stripe documents and generates responses using a Large Language Model (LLM).

The chatbot only answers questions related to Stripe documentation and avoids answering unrelated questions to reduce hallucinations.

---

Features

- Answers questions about Stripe documentation.
- Uses Retrieval-Augmented Generation (RAG).
- Performs semantic search using FAISS Vector Database.
- Provides an interactive chat interface using Streamlit.
- Supports topics such as:
  - Stripe API
  - API Keys
  - Payments
  - Payment Intents
  - Webhooks
  - Refunds
  - Checkout

---

Technologies Used

- Python
- LangChain
- FAISS
- Sentence Transformers
- Unsloth
- Llama 3.2 3B Instruct
- Streamlit

---

How It Works

1. Stripe documentation is collected and stored as Markdown files.
2. The documents are split into smaller chunks.
3. Embeddings are generated for each chunk.
4. The embeddings are stored in a FAISS vector database.
5. When a user asks a question, the system retrieves the most relevant document chunks.
6. The retrieved information is sent to the LLM.
7. The model generates an answer based only on the retrieved documentation.

---

Project Structure

```text
Stripe_RAG_Project/
│
├── data/
│   ├── raw_docs_md/
│   └── vector_db/
│
├── src/
│   ├── rag_pipeline.py
│   └── app.py
│
├── requirements.txt
└── README.md
```

> Note: The project can run on CPU, but responses may be much slower.

Installation

1. Clone the Repository

```bash
git clone <your-github-repository-link>
cd Stripe_RAG_Project
```

2. Create a Virtual Environment

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate

3. Install PyTorch

For NVIDIA GPU:

```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu128
```

For CPU (optional):

```bash
pip install torch(Without GPU it will work but will give answers quit slower )
```

4. Install Project Dependencies

```bash
pip install -r requirements.txt
```

---

Running the Project

Go to the source folder:

```bash
cd src
```

Run the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser at:

```text
http://localhost:8501
```



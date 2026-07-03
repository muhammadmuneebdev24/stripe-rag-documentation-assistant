
import os
import torch
from unsloth import FastLanguageModel
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

# ==================================================
# Device
# ==================================================
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")

# ==================================================
# Base Directory
# ==================================================
if os.path.exists("/content/drive/MyDrive/Stripe_RAG_Project"):
    BASE_DIR = "/content/drive/MyDrive/Stripe_RAG_Project"
else:
    BASE_DIR = os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )

VECTOR_DB_PATH = os.path.join(BASE_DIR, "data", "vector_db")

# ==================================================
# Load Embeddings
# ==================================================
print("Loading embeddings...")

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={"device": device},
)

# ==================================================
# Load FAISS
# ==================================================
print("Loading FAISS database...")

vector_db = FAISS.load_local(
    VECTOR_DB_PATH,
    embeddings,
    allow_dangerous_deserialization=True,
)

print("FAISS loaded successfully.")

# ==================================================
# Retriever
# ==================================================
retriever = vector_db.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 5}
)


# ==================================================
# Load LLM
# ==================================================
print("Loading Llama model...")

model, tokenizer = FastLanguageModel.from_pretrained(
    model_name="unsloth/Llama-3.2-3B-Instruct-bnb-4bit",
    max_seq_length=2048,
    dtype=None,
    load_in_4bit=True,
)

FastLanguageModel.for_inference(model)

print("Model loaded successfully.")

# ==================================================
# Main Function
# ==================================================
def ask_stripe(question, chat_history=None):

    # Retrieve relevant chunks
    docs = retriever.invoke(question)

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    sources = list(
        set(
            doc.metadata.get("source", "unknown")
            for doc in docs
        )
    )

    system_prompt = """
You are a Stripe Documentation Assistant.

Answer ONLY using the information provided in the context.

Rules:
1. Do not use outside knowledge.
2. If the answer exists in the context, answer clearly and concisely.
3. If the context does not contain enough information, respond exactly with:

I could not find that information in the Stripe documentation.
"""

    user_prompt = f"""
Context:
{context}

Question:
{question}

Answer using only the context above.
"""

    messages = [
        {
            "role": "system",
            "content": system_prompt,
        },
        {
            "role": "user",
            "content": user_prompt,
        },
    ]

    inputs = tokenizer.apply_chat_template(
        messages,
        tokenize=True,
        add_generation_prompt=True,
        return_tensors="pt",
    ).to(device)

    attention_mask = torch.ones_like(inputs)

    with torch.no_grad():
        outputs = model.generate(
            inputs,
            attention_mask=attention_mask,
            max_new_tokens=400,
            do_sample=False,
            repetition_penalty=1.05,
            pad_token_id=tokenizer.eos_token_id,
        )

    generated_tokens = outputs[0][inputs.shape[1]:]

    response = tokenizer.decode(
        generated_tokens,
        skip_special_tokens=True,
    ).strip()

    return {
        "answer": response,
        "sources": sources,
    }

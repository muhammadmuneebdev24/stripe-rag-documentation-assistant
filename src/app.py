import streamlit as st
from rag_pipeline import ask_stripe

st.set_page_config(
    page_title="Stripe Documentation Assistant",
    page_icon="💳"
)

st.title("💳 Stripe Documentation Assistant")
st.write("Ask questions about Stripe documentation.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

prompt = st.chat_input("Ask about Stripe...")

if prompt:
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.write(prompt)
    history = [msg["content"] for msg in st.session_state.messages if msg["role"] == "user"]
    result = ask_stripe(prompt, chat_history=history[:-1])
    answer = result["answer"]

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )

    with st.chat_message("assistant"):
        st.write(answer)

import streamlit as st

st.title("Simple RAG Chat App")

if "messages" not in st.session_state:
    st.session_state.messages = []

def simple_rag(query):
    if "hello" in query.lower():
        return "Hello! How can I help you?"
    elif "rag" in query.lower():
        return "RAG combines retrieval and generation for better responses."
    else:
        return f"You asked: '{query}'. A real RAG system would search documents and generate a response."

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask a question"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    response = simple_rag(prompt)
    st.session_state.messages.append({"role": "assistant", "content": response})

    with st.chat_message("assistant"):
        st.markdown(response)

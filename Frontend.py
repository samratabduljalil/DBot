import streamlit as st
import requests

# FastAPI backend URL
API_URL = "http://127.0.0.1:8000/query"

# Streamlit UI Setup
st.set_page_config(page_title="DBot", layout="centered")
st.title("🗃️ Welcome to DBot .")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
query = st.chat_input("Ask something about the database...")
if query:
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": query})
    with st.chat_message("user"):
        st.markdown(query)
    
    # Call FastAPI backend
    response = requests.get(API_URL, params={"question": query})
    response_data = response.json()
    bot_reply = response_data.get("response", {}).get("output", "Sorry, I couldn't process that.")
    
    # Display bot response
    with st.chat_message("assistant"):
        st.markdown(bot_reply)
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})

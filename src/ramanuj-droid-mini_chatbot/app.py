import streamlit as st
from responses import responses, default_response

st.set_page_config(page_title="ChatGPT-Like Rule-Based Chatbot", page_icon="🤖")

st.title("Mini-Chatbot")
if "messages" not in st.session_state:
    st.session_state.messages = []

def get_response(user_input):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return responses[key]
    return default_response


user_input = st.chat_input("Type your message...")

if user_input:
    # Append user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    # Get bot response
    bot_response = get_response(user_input)
    # Append bot message
    st.session_state.messages.append({"role": "bot", "content": bot_response})

for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.chat_message("user").write(msg["content"])
    else:
        st.chat_message("assistant").write(msg["content"])

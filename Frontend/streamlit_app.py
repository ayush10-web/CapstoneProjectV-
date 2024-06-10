import streamlit as st
import requests

st.title("ChatBot")

def get_response(message):
    response = requests.post("http://127.0.0.1:5000/chat", json={"message": message})
    return response.json().get("response")

if "messages" not in st.session_state:
    st.session_state.messages = []

with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("You:", "")
    submitted = st.form_submit_button("Send")

    if submitted and user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})
        response = get_response(user_input)
        st.session_state.messages.append({"role": "bot", "content": response})

for message in st.session_state.messages:
    if message["role"] == "user":
        st.write(f"You: {message['content']}")
    else:
        st.write(f"Bot: {message['content']}")

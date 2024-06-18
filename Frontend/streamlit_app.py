import streamlit as st
import requests

def get_response(message):
    url = 'http://localhost:5000/api/chat'  # Your backend URL
    data = {'message': message}
    try:
        response = requests.post(url, json=data)
        response_data = response.json()
        return response_data.get('response')
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    st.set_page_config(page_title="Q&A Demo")
    st.header("Chatbot")

    # Initialize session state for chat history if it doesn't exist
    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []

    input_message = st.text_input("Input: ", key="input")
    submit_button = st.button("Submit")

    if submit_button and input_message:
        response = get_response(input_message)
        st.subheader("Answer:")
        st.write(response)

        # Add user query and response to session state chat history
        st.session_state['chat_history'].append(("Your question", input_message))
        st.session_state['chat_history'].append(("Chatbot answer", response))

    st.subheader("The Chat History is")
    for role, text in st.session_state['chat_history']:
        st.write(f"{role}: {text}")

if __name__ == '__main__':
    main()

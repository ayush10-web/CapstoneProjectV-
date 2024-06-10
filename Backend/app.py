from flask import Flask, request, jsonify
from openai import ChatCompletion  # Import the appropriate class
from dotenv import load_dotenv
import os

app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get("message")
    response_message = generate_response(user_message)
    return jsonify({"response": response_message})

def generate_response(message):
    try:
        chat_completion = ChatCompletion.create(  # Use the appropriate method
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": message,
                }
            ],
        )
        return chat_completion.choices[0].message['content'].strip()
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(port=5000, debug=True)

from flask import Flask, request, jsonify # type: ignore
import google.generativeai as genai # type: ignore
import os

app = Flask(__name__)

# Assuming your environment variable is named GOOGLE_API_KEY
api_key = os.getenv("GOOGLE_API_KEY")

if api_key:
  genai.configure(api_key=api_key)
else:
  # Handle the case where the environment variable is not set (optional)
  # You can raise an error, log a warning, or provide a default behavior
  raise ValueError("GOOGLE_API_KEY environment variable not set")

# Initialize Gemini model
model = genai.GenerativeModel("gemini-pro")

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message')

    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    try:
        response = model.start_chat(history=[]).send_message(user_message, stream=True)
        response_text = "".join(chunk.text for chunk in response)
        return jsonify({"response": response_text.strip()})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
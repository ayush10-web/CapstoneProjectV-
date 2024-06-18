from flask import Flask, request, jsonify
from flask_restx import Api, Resource, fields
import google.generativeai as genai
import os

app = Flask(__name__)
api = Api(app, version='1.0', title='Chat API', description='Api')

ns = api.namespace('api', description='Chat operations')

chat_model = api.model('Chat', {
    'message': fields.String(required=True, description='The chat message')
})

response_model = api.model('ChatResponse', {
    'response': fields.String(description='The chat response')
})

error_model = api.model('Error', {
    'error': fields.String(description='Error message')
})

# Configure Google API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize Gemini model
model = genai.GenerativeModel("gemini-pro")

@ns.route('/chat')
class Chat(Resource):
    @ns.doc('chat')
    @ns.expect(chat_model, validate=True)
    @ns.response(200, 'Success', response_model)
    @ns.response(400, 'Validation Error', error_model)
    @ns.response(500, 'Internal Server Error', error_model)
    def get(self):
        '''Send a message and get a response'''
        data = request.json
        user_message = data.get('message')

        if not user_message:
            return {"error": "No message provided"}, 400

        try:
            response = model.start_chat(history=[]).send_message(user_message, stream=True)
            response_text = "".join(chunk.text for chunk in response)
            return {"response": response_text.strip()}, 200
        except Exception as e:
            return {"error": str(e)}, 500

if __name__ == '__main__':
    app.run(debug=True)

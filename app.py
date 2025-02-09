from flask import Flask, request, jsonify
import json
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize

app = Flask(__name__)

# Load knowledge base
with open("knowledge_base.json") as file:
    knowledge_base = json.load(file)

def chatbot_response(user_input):
    user_words = word_tokenize(user_input.lower())
    for question, answer in knowledge_base.items():
        if any(word in question.lower() for word in user_words):
            return answer
    return "Sorry, I don't understand. Please contact IT support."

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"]
    response = chatbot_response(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)



# Command : curl -X POST http://127.0.0.1:5000/chat -H "Content-Type: application/json" -d '{"message": "How do I reset my password?"}'
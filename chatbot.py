import json
import nltk
from nltk.tokenize import word_tokenize

# Load knowledge base
with open("knowledge_base.json") as file:
    knowledge_base = json.load(file)

def chatbot_response(user_input):
    user_words = word_tokenize(user_input.lower())  # Convert input to words
    for question, answer in knowledge_base.items():
        if any(word in question.lower() for word in user_words):
            return answer
    return "Sorry, I don't understand. Please contact IT support."

# Test the chatbot
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    response = chatbot_response(user_input)
    print("Bot:", response)
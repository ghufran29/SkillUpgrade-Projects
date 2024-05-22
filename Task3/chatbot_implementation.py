import spacy
from datetime import datetime


nlp = spacy.load("en_core_web_sm")


RESPONSES = {
    "hi": "Hello!",
    "hello": "Hi there!",
    "how are you": "I'm just a chatbot, but thanks for asking!",
    "what is your name": "You can call me ChatGPT!",
    "what is your purpose": "I'm here to assist you with basic tasks and answer questions.",
    "what time is it": datetime.now().strftime("%I:%M %p"),  
    "what day is it": datetime.now().strftime("%A, %B %d, %Y"),  
}


def get_response(input_text):
   
    doc = nlp(input_text.lower())
    
   
    if any(token.text in ["hi", "hello"] for token in doc):
        return RESPONSES["hi"]
    
   
    if any(token.text in ["time", "clock"] for token in doc):
        return RESPONSES["what time is it"]
    
   
    if any(token.text in ["day", "date", "calendar"] for token in doc):
        return RESPONSES["what day is it"]
    
   
    for key in RESPONSES:
        if key in input_text.lower():
            return RESPONSES[key]
    
   
    return "I'm sorry, I didn't understand that."


def main():
    print("Welcome to the Chatbot! You can start chatting. Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        response = get_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()

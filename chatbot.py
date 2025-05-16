import random

responses = {
    "hello": ["Hi there!", "Hello!", "Hey!"],
    "how are you": ["I'm fine, thank you!", "Doing great, how about you?"],
    "bye": ["Goodbye!", "See you later!", "Bye! Take care."],
    "default": ["I'm not sure I understand.", "Can you rephrase that?", "Interesting..."]
}

def get_response(user_input):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return random.choice(responses["default"])

if __name__ == "__main__":
    print("Chatbot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if "bye" in user_input.lower():
            print("Chatbot:", get_response("bye"))
            break
        print("Chatbot:", get_response(user_input))

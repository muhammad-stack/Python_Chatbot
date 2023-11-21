# Import necessary libraries
import random
from typing import Dict

# Define responses for different prompts
responses : Dict[str,list[str]]= {
    "hello": ["Hello!", "Hi there!", "Hey!"],
    "how_are_you": ["I'm doing well, thank you!", "I'm good. How about you?", "All good!"],
    "bye": ["Goodbye!", "See you later!", "Take care!"],
    "default": ["I'm sorry, I didn't quite catch that.", "Could you please rephrase?", "I'm still learning!"]
}

# Function to get a response based on user input
def get_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input:
        return random.choice(responses["hello"])
    elif "how are you" in user_input:
        return random.choice(responses["how_are_you"])
    elif "bye" in user_input:
        return random.choice(responses["bye"])
    else:
        return random.choice(responses["default"])

# Main loop for chatbot interaction
def main():
    print("Chatbot: Hello! How can I assist you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        response = get_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()

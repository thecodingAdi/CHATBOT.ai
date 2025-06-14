import re

def chatbot():
    print("Chatbot: Hello! I am a simple chatbot. Type 'quit' to exit.")
    while True:
        user_input = input("You: ").lower()

        if user_input in ['quit', 'exit', 'bye']:
            print("Chatbot: Goodbye! Have a great day!")
            break

        # Pattern matching and rule-based replies
        elif re.search(r'\b(hi|hello|hey)\b', user_input):
            print("Chatbot: Hi there! How can I help you?")

        elif re.search(r'\bhow are you\b', user_input):
            print("Chatbot: I'm just a bunch of code, but I'm doing great!")

        elif re.search(r'\bwhat.*your name\b', user_input):
            print("Chatbot: I'm ChatGPT-Basic, your simple assistant.")

        elif re.search(r'\b(bye|see you)\b', user_input):
            print("Chatbot: See you later!")

        elif re.search(r'\b(help|support)\b', user_input):
            print("Chatbot: Sure, I can try to help. What do you need?")

        elif re.search(r'\b(what.*time)\b', user_input):
            from datetime import datetime
            now = datetime.now()
            print(f"Chatbot: It's {now.strftime('%I:%M %p')}.")

        else:
            print("Chatbot: Sorry, I don't understand that. Try asking something else.")

# Run the chatbot
if __name__ == "__main__":
    chatbot()

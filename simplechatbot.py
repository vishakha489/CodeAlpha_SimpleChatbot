# Simple Rule-Based Chatbot

def chatbot():
    print("Chatbot: Hi! I'm your friendly chatbot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").lower()  # take user input and convert to lowercase

        if user_input == "hello":
            print("Chatbot: Hi there!")
        elif user_input == "how are you":
            print("Chatbot: I'm fine, thanks for asking! How about you?")
        elif user_input in ["bye", "exit", "quit"]:
            print("Chatbot: Goodbye! Have a great day! 👋")
            break
        elif user_input == "i am fine":
            print("Chatbot: That's great to hear!")
        elif user_input == "what is your name":
            print("Chatbot: I'm a simple Python chatbot.")
        else:
            print("Chatbot: Sorry, I didn’t understand that. Try saying 'hello' or 'how are you'.")

# Run the chatbot
chatbot()
def chatbot():
    print("👋 Hello! I'm ChatBot. Feel free to ask me anything, or type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if "hello" in user_input or "hi" in user_input:
            print("Bot: Hi there! How can I assist you today?")
        elif "your name" in user_input:
            print("Bot: I'm a simple rule-based chatbot created for an internship project.")
        elif "how are you" in user_input:
            print("Bot: I'm doing great, thanks for asking! How can I help you?")
        elif "bye" in user_input:
            print("Bot: Goodbye! It was nice talking to you. 😊")
            break
        else:
            print("Bot: I'm not sure how to respond to that yet. Could you ask something else?")

chatbot()
hi
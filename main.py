def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you?"
    elif "how are you" in user_input:
        return "I'm just a bot, But I'm here to help you!"
    elif "your name" in user_input:
        return "I'm chatbot"
    elif "what do you do" in user_input:
        return "I can answer your queries and provide information on various topics"
    elif "bye" in user_input:
        return "Bye..! Have a great day."
    else:
        return "I'm sorry, I do not understand what you are trying to say."
    
def main():
    print("Chatbot : Hi there! Type something to start chatting. Type 'bye' to exit.")
    while True:
        user_input = input("You : ")
        if "bye" in user_input.lower():
            print("Chatbot : Bye..! Have a great day.")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
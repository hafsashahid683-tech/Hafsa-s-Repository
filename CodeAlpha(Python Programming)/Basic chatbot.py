
def chatbot_response(user_input):
    # Convert input to lowercase for easier matching
    user_input = user_input.lower().strip()

    if user_input == "hello":
        return "Hi!"

    elif user_input == "how are you":
        return "I'm fine, thanks!"

    elif user_input == "bye":
        return "Goodbye!"

    else:
        return "Sorry, I don't understand that."


def main():
    print("Chatbot: Hello! Welcome to my chatbot.")
    print("Chatbot: Type 'bye' to end the conversation.")

    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print("Chatbot:", response)

        if user_input.lower().strip() == "bye":
            break


if __name__ == "__main__":
    main()

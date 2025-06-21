# Simple Rule-Based Chatbot

def chatbot_response(user_input):
    user_input = user_input.lower().strip()

    # Rule-based responses
    if user_input == "hello":
        return "Hi there! How can I help you today?"
    elif user_input == "how are you":
        return "I'm just a bunch of code, but I'm doing great! Thanks for asking!"
    elif user_input == "bye":
        return "Goodbye! Have a nice day."
    elif user_input == "what is your name":
        return "I’m AlphaBot, your virtual friend!"
    elif user_input == "help":
        return "You can say 'hello', ask 'how are you', or say 'bye' to end."
    else:
        return "Sorry, I didn’t understand that. Type 'help' for options."

# Main loop
print("🤖 Welcome to AlphaBot! Type 'bye' to end the chat.\n")

while True:
    user_message = input("You: ")
    response = chatbot_response(user_message)
    print("AlphaBot:", response)

    if user_message.lower() == "bye":
        break

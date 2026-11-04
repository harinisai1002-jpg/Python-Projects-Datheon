import re

print("=" * 40)
print("       WELCOME TO PYTHON CHATBOT")
print("=" * 40)

responses = {
    "hello": "Hello! Welcome. How can I help you?",
    "hi": "Hi there! How can I help you?",
    "hours": "Our business hours are 9 AM to 6 PM.",
    "products": "We offer laptops, mobiles and accessories.",
    "price": "Our prices depend on the product you choose.",
    "delivery": "Delivery usually takes 3 to 5 working days.",
    "return": "Products can be returned within 7 days.",
    "help": "You can ask me about products, prices, delivery or business hours."
}

print("\nBot: Hello! I am your assistant.")
print("Bot: Type 'bye' or 'exit' to end the conversation.")

while True:

    user_input = input("\nYou: ").lower().strip()

    if user_input in ["bye", "exit", "quit"]:
        print("Bot: Thank you for chatting. Goodbye!")
        break

    elif re.search(r"\b(hello|hi|hey)\b", user_input):
        print("Bot:", responses["hello"])

    elif re.search(r"\b(hours|timing|open|close)\b", user_input):
        print("Bot:", responses["hours"])

    elif re.search(r"\b(products|items|available)\b", user_input):
        print("Bot:", responses["products"])

    elif re.search(r"\b(price|cost|rate)\b", user_input):
        print("Bot:", responses["price"])

    elif re.search(r"\b(delivery|shipping)\b", user_input):
        print("Bot:", responses["delivery"])

    elif re.search(r"\b(return|refund)\b", user_input):
        print("Bot:", responses["return"])

    elif re.search(r"\b(help|support)\b", user_input):
        print("Bot:", responses["help"])

    else:
        print("Bot: Sorry, I didn't understand.")
        print("Bot: Please ask me something else.")
from config import ask_health_bot

print("HealthBot is ready! Type 'exit' to quit.")
while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit', 'bye']:
        print("Exiting HealthBot. Take care!")
        break
    response = ask_health_bot(user_input)
    print(f"Bot: {response}")
from llm import llm

print("🔮 Local Chatbot is ready! Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("👋 Goodbye!")
        break
    response = llm(user_input)
    print("AI:", response)

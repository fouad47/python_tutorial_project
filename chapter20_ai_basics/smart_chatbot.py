# A simple rule-based Chatbot

print("Hello! I am ChatBot-Mini. Talk to me!")

# A 'while True' loop runs forever! It keeps the chatbot awake.
while True:
    # We ask the user to type a message.
    message = input("You: ").lower()
    
    # If they type 'quit', we use 'break' to escape the infinite loop!
    if message == "quit":
        print("Bot: Goodbye! 👋")
        break
        
    # We use 'in' to check if a specific word is hidden inside their message.
    elif "hello" in message or "hi" in message:
        print("Bot: Hello human! 🤖")
        
    elif "how are you" in message:
        print("Bot: My circuits are feeling great today! ⚡")
        
    elif "joke" in message:
        print("Bot: Why did the computer squeak? Because someone stepped on its mouse! 🐁😂")
        
    # A catch-all response if the bot doesn't understand.
    else:
        print("Bot: Hmm, I am still learning. Tell me more!")

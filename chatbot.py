def chatbot():
    print("Chatbot: Hi! I'm your simple chatbot. Type 'bye' to exit")

    while True:
        user_input=input("You :").lower()

        if user_input=="bye":
            print("Chatbot: Goodbye! Have a nice day")
            break
        elif "who is priyanshu" in user_input:
            print("Chatbot: Priyanshu is your son")
        elif "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hello! How can I help you?")
        elif "how are you" in user_input:
            print("Chatbot: im just code, but im doing")
        elif "your name" in user_input:
            print("Chatbot: im simple python chatbot")
        elif "help" in user_input:
            print("Chatbot: i can chat with you")
        else:
            print("Chatbot: Sorry, I don't understand you" )
chatbot()

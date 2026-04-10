def doctor_chatbot():
    print("Doctor: Hello! I'm your virtual doctor. Type 'bye' to exit.")

    while True:
        patient = input("Patient: ").lower()

        if patient == "bye":
            print("Doctor: Take care! Stay healthy")
            break
        elif "hello" in patient or "hi" in patient:
            print("Doctor: Hello! Tell me your problem?")

        elif "how are you" in patient:
            print("Doctor: I'm here to help you feel better!")

        elif "fever" in patient:
            print("Doctor: You might have an infection. Please take rest and stay hydrated.")

        elif "cold" in patient or "cough" in patient:
            print("Doctor: It seems like a common cold. Drink warm water or tea and take medicine.")

        elif "headache" in patient:
            print("Doctor: Try resting in a quiet place and drink water.")

        elif "stomach pain" in patient:
            print("Doctor: Avoid spicy food and take proper rest. If pain increases, visit a clinic.")

        elif "vomit" in patient or "nausea" in patient:
            print("Doctor:eat light food and Stay hydrated.")

        elif "diarrhea" in patient:
            print("Doctor: Drink ORS and fluids. How many times are you going to the washroom?")

        elif "sore throat" in patient:
            print("Doctor: Do you have difficulty swallowing? Try warm salt water gargle.")

        elif "body pain" in patient:
            print("Doctor: This may be due to fatigue or infection. Are you feeling tired too?")

        elif "dizziness" in patient:
            print("Doctor: Are you eating properly and staying hydrated?")

        elif "fatigue" in patient or "tired" in patient:
            print("Doctor: Make sure you're getting enough sleep and nutrition.")

        elif "chest pain" in patient:
            print("Doctor: This could be serious. Please seek immediate medical attention!")

        elif "yes" in patient:
            print("Doctor: Okay, that helps. I recommend rest and proper medication.")

        elif "no" in patient:
            print("Doctor: Alright, monitor your symptoms and take care.")

        elif "thank you" in patient:
            print("Doctor: You're welcome!")

        else:
            print("Doctor:explain your symptoms in detail")

doctor_chatbot()
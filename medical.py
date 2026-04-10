from flask import Flask,request,jsonify,send_from_directory
app=Flask(__name__)

def get_response(user_input):
    
        user_input = user_input.lower()
        if user_input =="bye":
            return ("Chatbot: Take care! Stay healthy!")
        elif "hello" in user_input or "hi" in user_input:
            return ("Chatbot: Hello! How can I help you?")
        elif "what is your name" in user_input:
            return ("Chatbot: I'm a chatbot doctor.")
        elif "what is your specialization" in user_input:
            return ("Chatbot: I specialize in general medicine and can provide information on common health issues.")
        elif "what are your working hours" in user_input:
            return ("Chatbot: I am available 24/7 to assist you with your health-related questions.")     
        elif "can you help me with my symptoms" in user_input:
            return ("Chatbot: Of course!,tell me what problem do you have if you are feeling unwell?") 
        elif "headache" in user_input:
            return ("Chatbot: you're experiencing a headache. It could be caused by various factors such as stress," )
        elif "stress" in user_input:
                return ("Chatbot: stress can lead to tension headaches. Consider practicing relaxation techniques and managing stress levels.")
        elif "dehydration" in user_input:
                return ("Chatbot: dehydration can also cause headaches. Make sure to drink enough water throughout the day.")
        elif "eye strain" in user_input:
                return ("Chatbot: eye strain from prolonged screen time can contribute to headaches. Take regular breaks and adjust your screen settings.")
        elif "sideheadach" in user_input:
                return ("it may due to gas problem take pentop-D or take disprine")
        elif"stomach pain"in user_input:
             return ("chatbot:you have stomach pain it could cause my many factor")
        elif "its in upper stomach" in user_input:
              return ("it is due to gas problem i think you should take pentop-D or cyra-D or due to food poisining go hospital")
        elif "in rigth side of stomach"in user_input:
              return ("it is due to  problem in liver think you should take digonosis in hospital")
        elif "in left side of stomach"in user_input:
              return (" it is due problem in your pancrea due to sweeling i think you should go to hospital for digonosi")
        elif "in lower side of stomach"in user_input:
              return ("it is due problem in your intestine due to food poisining i think you should go to hospital for digonosis")
        elif"whole of stomach" in user_input:
              return ("go to hospital it could be a sever problem go for diginosis")

        elif "breathing problem" in user_input:
         return ("it is due problem of air pollution ,tuberclosis or due to asthma")
        elif "fever" in user_input:
         return ("Chatbot: You may have a fever. It can be due to infection or viral.")
    
        elif "cold" in user_input or "cough" in user_input:
         return ("Chatbot: It looks like you have cold or cough.")

        elif "sore throat" in user_input:
         return ("Gargle with warm salt water and avoid cold drinks.")

        elif "vomiting" in user_input or "nausea" in user_input:
         return ("Chatbot: You may have food poisoning or stomach infection.")

        elif "diarrhea" in user_input or "loose motion" in user_input:        
         return ("Chatbot: You are having loose motion.")
       
        elif "body pain" in user_input:
         return ("Chatbot: take paracetamol and rest")
            
        elif "back pain" in user_input:
              return ("Chatbot: Back pain may be due to bad posture or strain.")

        elif "chest pain" in user_input:
              return ("Chatbot: Chest pain can be serious.")
        elif"strain" in user_input:
            return ("i think it it due to excessive work so take rest")

        elif "dizziness" in user_input:
         return ("Chatbot: You may feel dizzy due to low BP or weakness.")
        

        elif "weakness" in user_input:
         return ("Chatbot: Weakness can be due to lack of nutrition or sleep.")        
        
        elif "skin rash" in user_input:
         return ("Chatbot: Skin rash may be due to allergy or infection.")
        else:
            return ("Chatbot: Give more details")

@app.route("/")
def home():
    return send_from_directory('.','medical8.html')

@app.route("/chat", methods=["POST"])
def chat():
    data=request.json
    user_message=data.get("message")
    response=get_response(user_message)
    return jsonify({"response": response})

if __name__== "__main__":
    print ("Chatbot is running! Visit http://127.0.0.1:5000 in your browser")
    print ("Serving medical8.html file")
    app.run(debug=True)

 


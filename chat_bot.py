responses={
    "hello":"Hello there!How may I help you?",
    "why someone built you":"they wanted to excel in python",
    "hi":"Hi there! At your service",
    "who are you":"I am EDITH,an AI chatbot built by Tony Stark",
    "what is your name":"My name is EDITH(Even Death I am hero)",
    "hello":"Hi there? How may I help you?",
    "bye":"Ok ,bye take care!",
    "goodbye":"good bye! have a great day",
}
def chat_res(user_input):
    user_input=user_input.lower()
    return responses.get(user_input,"Sorry I am not allowed to answer rubbish questions.Try Something new")

def main():
    print("Type bye or good bye to exit chat")
    while True:
        user_input=input("You:")
        res=chat_res(user_input)
        print("Chatbot:",res)
        if user_input.lower() in ["bye","goodbye"]:
            break
if __name__=="__main__":
    main()
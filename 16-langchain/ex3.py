from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage


def load_env():
    load_dotenv()

def initialize_llm():
    llm = ChatGoogleGenerativeAI(model = 'gemini-2.5-flash')
    return llm

def start_chat(llm):
    print("Assistant ready!")
    print("Type exit to quit")
    conversation =[SystemMessage(content="You ara a helpful ai assistant who answers questions politely and clearly")]
    while True:
        user_input = input("You: ")
        if user_input.strip().lower() == 'exit':
            print("\nHappy Learning! Bye.")
            break
        conversation.append(HumanMessage(content = user_input))
        response = llm.invoke(conversation)
        print("\nAI : ",response.content)
        conversation.append(AIMessage(content = response.content))
        print()

load_env()
llm = initialize_llm()
start_chat(llm)

from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from langchain_google_genai import (
    ChatGoogleGenerativeAI,
)
from dotenv import load_dotenv

load_dotenv()

#step 1 - Define state
class State(TypedDict):
    user_name:str
    greetings:str
    
#step 2 - Create LLM
llm = ChatGoogleGenerativeAI(model = 'gemini-2.5-flash')

#step 3 - node to accept input
def accept_input(state):
    print("accept_input called...")
    user_input = input("Enter your name : ")
    return {"user_name":user_input}
#step 4 - node to generate greeting
def generate_greetings(state):
    print("generate_greetings called...")
    prompt = f'Generate a short friendly greetings for this user : {state["user_name"]}'
    res = llm.invoke(prompt)
    return {"greetings":res.content}  

#step 5 - Build the graph
builder = StateGraph(State) 

#step 6 - add nodes
builder.add_node('accept_input',accept_input)
builder.add_node('generate_greetings',generate_greetings)


#step 7 - define graph flow
builder.add_edge(START,"accept_input")
builder.add_edge("accept_input","generate_greetings")
builder.add_edge("generate_greetings",END)


#step 8 - compile
graph = builder.compile()

#step 9 - execute
result = graph.invoke({})
print(result)


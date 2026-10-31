from typing import TypedDict
from langgraph.graph import StateGraph

#step 1 - Define state
class State(TypedDict):
    msg:str
    
#step 2 - Define nodes
def greet(state):
    print("greet called...")
    myDict = {'msg':'hello'}
    return myDict  

def add_name(state):
    print("add_name called...")
    strg = state["msg"] + ' Sachin'
    return {'msg':strg}  

def add_surname(state):
    print("add_surname called...")
    strg = state["msg"] + ' Kapoor'
    return {'msg':strg} 

def add_welcome(state):
    print("add_welcome called...")
    strg = state["msg"] + ', Welcome'
    return {'msg':strg} 

#step 3 - Build the graph
builder = StateGraph(State) 

#step 4 - add nodes
builder.add_node('greet',greet)
builder.add_node('name',add_name)
builder.add_node('surname',add_surname)
builder.add_node('welcome',add_welcome)

#step 5 - setup entry point
builder.set_entry_point("greet")

#step 6 - add edges
builder.add_edge("greet","name")
builder.add_edge("name",'surname')
builder.add_edge("surname",'welcome')
builder.add_edge("welcome",'__end__')

#step 7  - compile
graph = builder.compile()

#step 8 - execute
result = graph.invoke({})
print(type(result))
print(result)


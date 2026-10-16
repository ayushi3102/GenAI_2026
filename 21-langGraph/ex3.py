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

def router(state):
    if len(state['msg'])<20:
        return 'continue'
    return 'stop'

#step 3 - Build the graph
builder = StateGraph(State) 

#step 4 - add nodes
builder.add_node('greet',greet)
builder.add_node('add_name',add_name)

#step 5 - setup entry point
builder.set_entry_point("greet")

#step 6 - add edges
builder.add_edge("greet","add_name")
builder.add_conditional_edges("add_name",router,{
    'continue':'add_name',
    'stop':'__end__'})


#step 7  - compile
graph = builder.compile()

#step 8 - execute
result = graph.invoke({})
print(result)


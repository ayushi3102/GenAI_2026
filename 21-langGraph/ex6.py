from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from langchain_google_genai import (
    ChatGoogleGenerativeAI,
)
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv

load_dotenv()

#step 1 - Define state
class State(TypedDict):
    topic:str
    poem:str
    feedback:str
    retries:int
    
#step 2 - Create LLM
llm = ChatGoogleGenerativeAI(model = 'gemini-2.5-flash')

#step 3 - node to accept topic
def accept_topic(state):
    print("accept_topic called...")
    user_input = input("Enter your topic : ")
    return {"topic":user_input,'feedback':"",'retries':0}

#step 4 - node to generate poem
def generate_poem(state):
    print("generate_poem called...")
    prompt = f'Write a poem about {state["topic"]} '
    if(state['feedback']):
        prompt+=f'\n\n Prevous attempt feedback : \n {state["feedback"]} \n Please correct the mistake'
    res = llm.invoke([HumanMessage(content = prompt )])
    return {"poem":res.content, 'retries': state['retries']+1} 

def checker_node(state):
    print("checker_node called...")
    lines = [line.strip() for line in state['poem'].splitlines() if line.strip()]
    if len(lines) == 2 :
        return {'feedback':'perfect'}
    else:
        return {'feedback':f'current poem has {len(lines)} . I need only 2 '}

# Decision maker
def should_repeat(state):
    if state['feedback']=='perfect' or state['retries'] == 3:
        return 'end'
    else:
        return 'continue'
        

#step 5 - Build the graph
builder = StateGraph(State) 

#step 6 - add nodes
builder.add_node('accept_topic',accept_topic)
builder.add_node('generate_poem',generate_poem)
builder.add_node('checker_node',checker_node)


#step 7 - define graph flow
builder.add_edge(START,"accept_topic")
builder.add_edge("accept_topic","generate_poem")
builder.add_edge("generate_poem",'checker_node')
builder.add_conditional_edges("checker_node",should_repeat, {
    'continue':'generate_poem',
    'end': END
    })


#step 8 - compile
graph = builder.compile()

#step 9 - execute
result = graph.invoke({})
print(result)


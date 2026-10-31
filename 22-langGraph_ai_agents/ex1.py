from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from langchain_google_genai import (
    ChatGoogleGenerativeAI,
)
from dotenv import load_dotenv

# Target - if user ask a math ques then, through calculator tools ans should return else generate ans from llm

load_dotenv()

# 1 - Define State
class State(TypedDict):
    query:str
    decision:str
    final_result:str

# 2 - Create llm
llm =  ChatGoogleGenerativeAI(model = 'gemini-2.5-flash')

# 3 - Define nodes
def calculator(state):
    print("Running calculator...")
    try:
        result = eval(state['query'])
        return {'final_result':result}
    except:
        return {'final_result':'error'}
def generate_ans(state):
    print("Running generate_ans...")
    response = llm.invoke(state['query'])
    return {'final_result':response.content}

def decide_action(state):
    print("Running decide_action...")
    prompt = f"""
    Decide what to do for this query : {state['query']},
    If it requires calculations then return "tool" otherwise return "answer"
    """
    response = llm.invoke(prompt)
    strg = response.content.strip().lower()
    if 'tool' in strg:
        return {'decision':'tool'}
    else:
        return {'decision':'answer'}

def route(state):
    print(f"Running route, decision goes to '{state['decision']}'")
    if  state['decision'] == 'tool':
        return 'tool'
    return 'answer'


# 4 - build graph
builder = StateGraph(State)

# 5 - Add nodes
builder.add_node('decide',decide_action)
builder.add_node('tool',calculator)
builder.add_node('answer',generate_ans)

# 6 - set entry point and end point
builder.add_edge(START,"decide")
builder.add_conditional_edges("decide",route, {
    'tool':'tool',
    'answer': 'answer'
    })
builder.add_edge("tool",END)
builder.add_edge("answer",END)

# 7 - Accept input
topic = input("Enter youe ques: ")

# 8  - compile
graph = builder.compile()

# 9  - invoke
result = graph.invoke({'query':topic,'decision':'',"final_result":''})
print("Final ans-->\n",result['final_result'])



        
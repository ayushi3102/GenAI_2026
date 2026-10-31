import streamlit as st
from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from langchain_google_genai import (
    ChatGoogleGenerativeAI,
)
from tavily import TavilyClient
from dotenv import load_dotenv
import os 

load_dotenv()



# 1 - Define State
class AgentState(TypedDict):
    query:str
    decision:str
    final_result:str

# 2 - Create llm and tavily
llm =  ChatGoogleGenerativeAI(model = 'gemini-2.5-flash')
tavily = TavilyClient(api_key = os.getenv('TAVILY_API_KEY'))

# 3 - Define nodes
def web_search_tool(state):
    print("Running web search...")
    try :
        result = tavily.search(query =state['query'],max_result = 3)
        content = ''
        for r in result['results']:
            content+= f"{r['content']}\n\n"
        if 'weather' in state['query'].lower():
            prompt = f"""Extract weather details and format like this: 
            Location : 
            Temperature:
            Humidity:
            Wind Speed:
            Data {content}
            Do not give back the data that i am passing
            """
        else:
            prompt = f"""
            convert this into a clean and readable ans {content}
            """
        res = llm.invoke(prompt)
        return {
            'final_result':res.content
        }
    except:
        return {
            'final_result':"Seacrh failed! Try later"
        }
              
def calculator(state):
    print("Running calculator...")
    try:
        result = eval(state['query'])
        return {'final_result':result}
    except:
        return {'final_result':'error'}
def summarize_text(state):
    print("Running summarize_text...")
    response = llm.invoke(f"Summarize the text - {state['query']}")
    return {'final_result':response.content}

def generate_ans(state):
    print("Running generate_ans...")
    response = llm.invoke(state['query'])
    return {'final_result':response.content}

def decide_action(state):
    print("Running decide_action...")
    prompt = f"""
    Decide what to do for this query : {state['query']},
    If it requires calculations then return "tool",
    else if it requires to summarize the text then return 'summarize',
    else if it requires to do web search then return 'web_search'
    else return "answer"
    """
    response = llm.invoke(prompt)
    strg = response.content.strip().lower()
    if 'tool' in strg:
        return {'decision':'tool'}
    elif 'summarize' in strg:
        return  {'decision':'summarize'}
    elif 'web_search' in strg:
        return  {'decision':'web_search'}
    else:
        return {'decision':'answer'}

def route(state):
    print(f"Running route, decision goes to '{state['decision']}'")
    if  state['decision'] == 'tool':
        return 'tool'
    elif state['decision'] == 'summarize':
        return 'summarize'
    elif state['decision'] == 'web_search':
        return 'web_search'
        
    return 'answer'


# 4 - build graph
builder = StateGraph(AgentState)

# 5 - Add nodes
builder.add_node('decide',decide_action)
builder.add_node('tool',calculator)
builder.add_node('answer',generate_ans)
builder.add_node('summarize',summarize_text)
builder.add_node('web_search',web_search_tool)

# 6 - set entry point and end point
builder.add_edge(START,"decide")
builder.add_conditional_edges("decide",route, {
    'tool':'tool',
    'answer': 'answer',
    'summarize':'summarize',
    'web_search':'web_search'
    })
builder.add_edge("tool",END)
builder.add_edge("answer",END)
builder.add_edge("summarize",END)
builder.add_edge("web_search",END)

# 7 - Accept input
topic = input("Enter your ques: ")

# 8  - compile
graph = builder.compile()

# 9  - invoke
result = graph.invoke({'query':topic,'decision':'',"final_result":''})
print("Final ans-->\n",result['final_result'])



        
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_community.callbacks import get_openai_callback

load_dotenv()

def llm_initialize():
    llm = ChatOpenAI(model = 'gpt-4o-mini')
    return llm

llm = llm_initialize()

with get_openai_callback() as cb:
    response= llm.invoke("Where is taj mahal located?")
    print(response.content)
    print("Total tokens:",cb.total_tokens)
    print("Total input tokens:",cb.prompt_tokens)
    print("Total output tokens:",cb.completion_tokens)
    print("Total cost(USD):",cb.total_cost)
    print("Total cost(INR):",round(cb.total_cost*94.49,4))





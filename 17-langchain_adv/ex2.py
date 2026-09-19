from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

def llm_initialize():
    llm = ChatGoogleGenerativeAI(model = 'gemini-2.5-flash')
    return llm

llm = llm_initialize()

def calculate_cost(input_token,output_token,model):
    prices={
        "gemini-2.5-flash":{'input':0.30,'output':2.5},
        "gemini-3-flash":{'input':0.50,'output':3.0}
    }
    price = prices.get(model)
    input_cost = (price.get('input')*input_token)/1000000
    output_cost = (price.get('output')*output_token)/1000000
    print("Total cost (USD):", input_cost + output_cost)
    print("Total cost (INR):", round((input_cost + output_cost)*94.49,4))



response= llm.invoke("Where is taj mahal located?")

print(response.content)
print()
print(response.usage_metadata)

cb = response.usage_metadata

print("Total tokens:",cb['total_tokens'])
print("Total input tokens:",cb['input_tokens'])
print("Total output tokens:",cb['output_tokens'])

calculate_cost(cb['input_tokens'],cb['output_tokens'],'gemini-2.5-flash')







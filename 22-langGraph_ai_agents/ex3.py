from tavily import TavilyClient
from langchain_google_genai import (
    ChatGoogleGenerativeAI,
)
from dotenv import load_dotenv
import os 

load_dotenv()
tavily = TavilyClient(api_key = os.getenv('TAVILY_API_KEY'))

result = tavily.search(query ='current weather in bhopal',max_result = 1)
for r in result['results']:
    print('Title :',r['title'])
    print('Content :',r['content'])
    print('Url :',r['url'])
    print('\n')
    

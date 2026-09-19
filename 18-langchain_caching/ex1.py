from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.globals import set_llm_cache
from langchain_core.caches import InMemoryCache

load_dotenv()
#In memory cache enabled.
set_llm_cache(InMemoryCache())
llm = ChatGoogleGenerativeAI(model = 'gemini-2.5-flash')
ai_msz = llm.invoke('where is taj mahal')
print("Reply 1 : ",ai_msz.content)
print()

ai_msz = llm.invoke('where is taj mahal')
print("Reply 2 : ",ai_msz.content)
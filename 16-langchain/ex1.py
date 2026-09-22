from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
llm = ChatOpenAI(model = 'gpt-4o-mini')
ai_message = llm.invoke('where is taj mahal located?')
print(ai_message.content)

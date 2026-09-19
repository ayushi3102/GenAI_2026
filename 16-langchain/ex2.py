from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()
llm = ChatGoogleGenerativeAI(model = 'gemini-2.5-flash')
ai_message = llm.invoke('where is taj mahal located?')
print(ai_message.content)
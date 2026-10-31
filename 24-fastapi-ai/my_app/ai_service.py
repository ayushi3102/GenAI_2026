
from langchain_google_genai import (
    ChatGoogleGenerativeAI,
)
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()
class AIService:
    def __init__(self):
        
        self.llm =  ChatGoogleGenerativeAI(model = 'gemini-2.5-flash')
    def get_response(self,text:str):
        tem = ChatPromptTemplate.from_messages([('system','You are a professional techinal consultant. Answer in brief'),('human','{user_input}')])
        chain = tem | self.llm
        response = chain.invoke({'user_input':text})
        return response.content







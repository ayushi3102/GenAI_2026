from fastapi import FastAPI
from pydantic import BaseModel
from langchain_google_genai import (
    ChatGoogleGenerativeAI,
)
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

app = FastAPI()

llm =  ChatGoogleGenerativeAI(model = 'gemini-2.5-flash')

class Question(BaseModel):
    question:str
    


    
@app.post('/ask')
def ask(q:Question):
    tem = ChatPromptTemplate.from_messages([('system','You are a professional techinal consultant. Answer in brief'),('human','{user_input}')])
    chain = tem | llm
    response = chain.invoke({'user_input':q.question})
    return {'answer': response.content}



from fastapi import FastAPI
from pydantic import BaseModel
from langchain_google_genai import (
    ChatGoogleGenerativeAI,
)
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

llm =  ChatGoogleGenerativeAI(model = 'gemini-2.5-flash')

class Question(BaseModel):
    question:str
    
@app.post('/ask')
def ask(q:Question):
    response = llm.invoke(q.question)
    return {'answer': response.content}



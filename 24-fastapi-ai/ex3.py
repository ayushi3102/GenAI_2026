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
    

@app.post('/summarize')
def summarize(q:Question):
    tem = ChatPromptTemplate.from_template("Summarize this : {user_input}")
    chain = tem | llm
    response = chain.invoke({'user_input':q.question})
    return {'answer': response.content}
    
@app.post('/translate')
def translate(q:Question):
    tem = ChatPromptTemplate.from_template('Just Translate this message to hindi: {user_input}')
    chain = tem | llm
    response = chain.invoke({'user_input':q.question})
    return {'answer': response.content}



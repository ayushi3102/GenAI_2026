from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from ai_service import AIService

app = FastAPI()
ai_service = AIService()

class Question(BaseModel):
    question:str
    
@app.post('/ask')
def ask(q:Question):
    result = ai_service.get_response(q.question)
    return {'answer': result }



from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from ai_service import AIService

app = FastAPI()
ai_service = AIService()

class Question(BaseModel):
    question:str
    
@app.post('/ask')
async def ask(q:Question):
    if not q.question.strip():
            raise HTTPException(status_code =400,detail = "Topic cannot be blank")
    try:   
        result =await ai_service.get_response(q.question)
        return {'answer': result }
    except Exception as ex:
            raise HTTPException('status_code=503',detail = str(ex))



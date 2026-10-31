from fastapi import FastAPI,Query
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    username:str
    email:str
    age:int


# Request body

@app.post('/products')
def create_user(user : User):
    return {'message':'user created successfully','username':user.username}

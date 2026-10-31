from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def read_root():
    return {"message":"hello world"}

#path parameters

@app.get('/users/{id}')
def read_root(id:int):
    return {"id":id}

@app.get('/users/{id}/orders/{order_id}')
def read_root(id:int,order_id:int):
    return {"id":id,'order_id':order_id}
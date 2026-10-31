from fastapi import FastAPI,Query


app = FastAPI()

# Query parameter

@app.get('/products')
def get_products(category :str):
    return {"category":category}

@app.get('/products')
def get_products(category : list[str] = Query(default=[])):
    return {"category":category}

# Query(default=[]) = this tells list can be optional.
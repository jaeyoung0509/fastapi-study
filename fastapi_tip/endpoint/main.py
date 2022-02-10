from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def index():
    return {"hi" : "hi"}

@app.get('/{id}')
async def order_is_important(id: int):
    return {"return" : id}

@app.get('/message')
async def order_is_important():
    return {"return" : "message"}
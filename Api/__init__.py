from fastapi import FastAPI
from pydantic import BaseModel

class Article(BaseModel):
    id:int
    title:str
    dsecription:str
data = [ {"f" : "a"} , {"f" : "a"}]

app = FastAPI()

@app.get('/')
async def Index():
    return {"meesage" : "hello world"}

@app.get('/articles/')
def get_article(skip:int=0 , limit:int=20):
    return data[skip : skip + limit]

@app.post('/article/')
def add_article(artcle:Article):
    return artcle
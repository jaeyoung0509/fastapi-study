
from typing import List
from fastapi import Depends , FastAPI ,HTTPException , status
from sqlalchemy.orm import Session
from schemas import Item

app = FastAPI()

fake_db = {
    "foo": {"id": 1, "title": "Foo", "description": "There goes my hero"},
    "bar": {"id": 2, "title": "Bar", "description": "The bartenders"},
}


@app.get('/')
async def index():
    return {"msg" : "hello"}

@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: str):
    if item := fake_db.get(item_id ,None) == None:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND)
    return item

@app.post("/items", response_model =  Item)
async def create_item(item : Item):
    if fake_db.key(item.id) != None:
        raise HTTPException(status_code=400, detail="Item already exists")
    fake_db[item.id] = item
    return item

from turtle import title
from typing import Optional
from pydantic import BaseModel

class ItemBase(BaseModel):
    title : str 
    description :Optional[str] = None

class ItemCreate(ItemBase):
    ...

class Item(ItemBase):
    id : str
    class Config:
        orm_mode = True
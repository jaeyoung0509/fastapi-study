from datetime import timedelta
from typing import Any, List
from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from schemas.item import Item
from service import servie_item
router = APIRouter()

@router.get("/" , response_model= List[Item])
async def read_items( db : Session = Depends() , skip :int = 0 , limit : int = 100):
    items  = servie_item.item.get_multi(db , skip=skip , limit= limit)
    return items

@router.post("/" , response_model= Item)
def create_item() :
    pass
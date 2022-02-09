from fastapi import  status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session  
from database import get_db
import models , schemas
from utils.hash import hash , verify
from typing import List
router = APIRouter(
    prefix="/users" ,
    tags = ["users"] 
)   

@router.post("/" , status_code= status.HTTP_201_CREATED ,response_model= schemas.UserOut)
async def create_user(user: schemas.UserBase , db : Session = Depends(get_db)):
    hashed_password = hash(user.password)
    user.password = hashed_password
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/" , response_model=  List[schemas.UserBase])
async def get_alluser(db:Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users

@router.get("/{id}"  , response_model= schemas.UserOut)
async def get_user (id : int , db : Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                detail=f"user{id} is not found")
    return user

@router.delete("/{id}" )
async def dlete_user(id : int , db : Session = Depends(get_db)):
    pass
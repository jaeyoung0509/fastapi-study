from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List,Optional
import models , schemas , oauth2
from database import get_db

router = APIRouter(
    prefix="/post" ,
    tags=["post"]
)

@router.get('/' , response_model=List[schemas.PostOut])
async def get_posts(db:Session = Depends(get_db) , current_user : int = Depends(oauth2.get_current_user) , limit: int = 10  , skip : int = 0  , search : Optional[str] =""):
    posts = db.query(models.Post).all()
    return posts

@router.post('/' , response_model=schemas.Post)
async def create_post(req : schemas.PostCreate , db : Session = Depends(get_db)  , current_user : int  = Depends(oauth2.get_current_user)):
    new_post = models.Post(owner_id = current_user.id , **req.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post 
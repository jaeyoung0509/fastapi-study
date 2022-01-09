from typing import Optional
from pydantic import BaseModel

class ArticleSchemaIn(BaseModel):
    title :str
    description:str

class ArticleSchema(ArticleSchemaIn):
    id: int

class UserSchemaIn(BaseModel):
    username:str
    password:str

class UserSchema(BaseModel):
    id:int
    username:str

class LoginSchema(BaseModel):
    username:str
    password:str

class TokenData(BaseModel):
    username: Optional[str] = None
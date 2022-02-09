from typing import Optional 
from pydantic import BaseModel ,EmailStr
from datetime import datetime
from pydantic.types import conint

'''
UserSchema
id = Column(Integer , primary_key= True)
    email =Column(String , nullable= True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
'''

class UserBase(BaseModel):
    email : str
    password : str
    class Config:
        orm_mode =True

class UserOut(BaseModel):
    created_at : datetime
    email : str
    class Config:
        orm_mode =True


class PostBase(BaseModel):
    title : str
    content :str
    published : bool =True

    class Config:
        orm_mode =True

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserBase

class PostOut(BaseModel):
    Post: Post


'''
TokenData
'''
class Token(BaseModel):
    access_token :str 
    token_type = str

class Token_data(BaseModel):
    id : Optional[str] = None

'''
conint = type 강제하는것
Arguments to conint🔗
The following arguments are available when using the conint type function
'''

class Votes(BaseModel):
    post_id : int
    dir : conint(le=1)

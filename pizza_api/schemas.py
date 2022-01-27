from optparse import Option
from pydantic import BaseModel
from typing import Optional

from sqlalchemy import true



class SignupModel(BaseModel):
    id : Optional[int]
    username : str
    email : str
    password : str
    is_staff: Optional[bool]
    is_active: Optional[bool]

    class Config:
        orm_mode =True
        schema_extra ={
            'example' :{
                "username" : "jaeyoung",
                "email" : "jaeyoung@naver.com",
                "password" : "password" ,
                "is_staff" : False , 
                "is_active"  : True
            }
        }

class Settings(BaseModel):
    authjwt_secret_key :str = '8cd273c3a3bd27d7e28c96c75f1f5fa48653e1a49d031e35b378bc6d2d92a5b3'

class LoginModel(BaseModel):
    username: str
    password: str

class OrderModel(BaseModel):
    id : Optional[int]
    quantity : int
    order_status : Optional[str] ="PENDING"
    pizza_size : Optional[str] = "SMALL"
    user_id : Optional[int]
    
    class Config:
        orm_mode = True
        schema_extra = {
            "example" :{
                "quantity" : 2 ,
                "pizza_size" : "LARGE" ,

            }
        }
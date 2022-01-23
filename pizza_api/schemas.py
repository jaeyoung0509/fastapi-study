from pydantic import BaseModel
from typing import Optional

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
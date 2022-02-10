from pydantic import BaseModel

class User(BaseModel):
    id: int
    name : str
    email : str
    password : str
    '''
    orm_mode를 통해 sqlalchemy orm객체를 -> pydantic으로 변환 해
    response_model = pydantic_model로 정의 가능
    '''
    class Config:
        orm_mode = True

class PostBase(BaseModel):
    title : str
    content : str
    published : str
    class Config:
        orm_mode =True
'''
* pydantic BaseModel을 상속받은 클래스를 재 상속 가능
* 주의: 스크립트 언어이기 떄문에 부모 클래스를 위에 기술 해야 됨
'''
class Postcreate(PostBase):
    owner_id : int 
    owner : User
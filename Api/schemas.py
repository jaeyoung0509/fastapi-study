from pydantic import BaseModel


class ArticlesSchema(BaseModel):
    title : str
    description :str

class MyArticleSchema(ArticlesSchema):
    title:str
    description:str

    class Config:
        orm_mode =True
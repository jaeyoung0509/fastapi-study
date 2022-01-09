from os import stat
from fastapi import FastAPI , status
from fastapi.exceptions import HTTPException
from .models import Article_Pydantic , ArticleIn_Pydantic ,Article
from tortoise.contrib.fastapi import HTTPNotFoundError , register_tortoise
from typing import List
from pydantic import BaseModel
app =FastAPI()

class Status(BaseModel):
    message:str


@app.get('/articles/{id}', responses={404 : {"model" : HTTPNotFoundError}} , response_model= Article_Pydantic)
async def get_details(id:int):
    return await Article_Pydantic.from_queryset_single(Article.get(id=id))

@app.get('/articles' , response_model=List[Article_Pydantic])
async def get_artilce():
    return await Article_Pydantic.from_queryset(Article.all())

@app.post('/articles' , response_model = Article_Pydantic)
async def insert_article(article : ArticleIn_Pydantic):
    article_obj = await Article.create(**article.dict(exclude_unset= True))
    return await Article_Pydantic.from_tortoise_orm(article_obj)    


@app.put('/articles/{id}', responses={404 : {"model" : HTTPNotFoundError}} , response_model= Article_Pydantic)
async def update_aritlce(id:int , article:ArticleIn_Pydantic):
    await Article.filter(id=id).update(**article.dict(exclude_unset=True))
    return await Article_Pydantic.from_queryset_single(Article.get(id=id))

@app.delete('/articles/{id}', responses={404 : {"model" : HTTPNotFoundError}} , response_model= Status)
async def delete_aritlce(id:int):
    delete_aritlce = await Article.filter(id=id)
    if not delete_aritlce:
       raise HTTPException(stauts_code = status.HTTP_404_NOT_FOUND ,
       detail= f"user {id} not found")
    return Status(message= f"Deleted article {id}")
#postgres://postgres:pass@db.host:5432/somedb
register_tortoise(
    app , 
    db_url=  "postgres://postgres:root@localhost/tortoise_orm",
    modules={"models":["with_tortoise_api.models"]},
    generate_schemas = True, 
    add_exception_handlers=True
)
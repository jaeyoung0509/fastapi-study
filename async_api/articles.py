from fastapi import APIRouter, status , HTTPException , Depends
from .Schemas import ArticleSchemaIn , ArticleSchema, UserSchema
from typing import List
from .db import  Article ,database
from .Token import get_current_user


router =APIRouter(
    tags=["Articles"]
)


@router.post('/articles' ,status_code= status.HTTP_201_CREATED , response_model= ArticleSchema)
async def insert_artcile(article:ArticleSchemaIn):
    query = Article.insert().values(title = article.title , description = article.description)
    last_record_id  = await database.execute(query)
    return{**article.dict() , "id" : last_record_id}

     
@router.get('/articles/' , response_model= List[ArticleSchema])
async def get_articles(current_user:UserSchema = Depends(get_current_user)):
    query = Article.select()
    return await database.fetch_all(query = query)

@router.get('/articles/{id}' , response_model= ArticleSchema)
async def get_details(id :int):
    query = Article.select().where(id == Article.c.id)
    myarticle = await database.fetch_one(query=query)

    if not myarticle:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=  "Article is not found")
    return {**myarticle}

@router.put('/articles/{id}', response_model= ArticleSchema)
async def update_article(id:int ,article:ArticleSchemaIn):
    query = Article.update().where(Article.c.id == id).values(title =article.title,description = article.description)
    await database.execute(query)
    return {**article.dict() ,"id":id }


@router.delete('/articles/{id}',status_code=status.HTTP_204_NO_CONTENT)
async def delete_article(id:int):
    query =Article.delete().where(Article.c.id == id)
    await database.execute(query) 
    return {"message" : "article deleted"}
from fastapi.params import Depends
from sqlalchemy.orm import Session
from fastapi import FastAPI ,status , HTTPException
from sqlalchemy.sql.functions import mode
from .database import engine , sessionLocal
from .import Article, models 
from .schemas import ArticlesSchema , MyArticleSchema
from typing import List

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/articles' , response_model=List[MyArticleSchema])
def get_article(db:Session = Depends(get_db)):
    my_articles = db.query(models.Article).all()
    if my_articles:
        return my_articles
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail ="The aritcle doesn't exsist")

@app.get('/articles{id}' , status_code = status.HTTP_200_OK)
def article_details(id:int ,db:Session = Depends(get_db)):
    myarticle = db.query(models.Article).filter(models.Article.id==id).first()
    return myarticle

@app.post('/articles/' ,status_code= status.HTTP_201_CREATED , response_model=List[MyArticleSchema])
def add_article(article:ArticlesSchema ,db:Session = Depends(get_db)):
    new_article = models.Article(title=article.title  , description=article.description)
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return new_article
@app.put('/articles/{id}' , status_code=status.HTTP_202_ACCEPTED)
def update_article(id , article: ArticlesSchema  , db:Session = Depends(get_db)):
    db.query(models.Article).filter(models.Article.id==id).update({
        'title':article.title,
        'description':article.description
    })
    return {'message': 'The data is updated'}

@app.delete('/articles/{id}' ,status_code= status.HTTP_204_NO_CONTENT)
def delete_article(id:int , db:Session =Depends(get_db)):
    db.query(models.Article).filter(models.Article.id == id).delete(synchronize_session= False)
    db.commit()
from sqlalchemy import (
    Column , Integer , MetaData , String , Table , create_engine, engine
)
from databases import Database
DATABASE_URL = 'postgresql://postgres:root@localhost/article_db'

engine = create_engine(DATABASE_URL)
metadata = MetaData()
Article = Table(
    "article",
    metadata,
    Column("id" , Integer , primary_key= True) ,
    Column("title" , String(100)),
    Column("description" , String(100))
    
)

User = Table(
    "user",
    metadata,
    Column("id" , Integer , primary_key= True) ,
    Column("username" , String(20)),
    Column("password" , String(1000 ))
    
)  
database = Database(DATABASE_URL)
from click import echo
from sqlalchemy  import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = 'postgresql://postgres:root@localhost/blog_db'
engine = create_engine(DATABASE_URL , echo =True)

Base = declarative_base()
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False,)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
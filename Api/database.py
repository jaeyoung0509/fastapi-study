from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import session, sessionmaker


SQLALCHEMY_DATABASE_URL =  'postgresql://postgres:root@localhost/fastapi'
engine = create_engine(SQLALCHEMY_DATABASE_URL)
sessionLocal = sessionmaker(autocommit=False , autoflush= False , bind=engine)

Base = declarative_base()
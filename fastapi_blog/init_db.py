
from database import engine  ,Base
from models import User, Votes ,Post

Base.metadata.create_all(bind=engine)
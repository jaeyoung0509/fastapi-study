from xml.etree.ElementInclude import include
from fastapi import  FastAPI
from routers import user , auth , post ,votes
app = FastAPI()
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(post.router)
app.include_router(votes.router)
@app.get('/')
def index():
    return {"message:" :"hello world"}



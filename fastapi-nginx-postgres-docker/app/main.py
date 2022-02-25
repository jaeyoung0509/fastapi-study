from fastapi import FastAPI 
'''
gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 127.0.0.1:80
'''


app = FastAPI()

@app.get('/')
def root():
    return {'message'  : 'hello world'}
from fastapi import FastAPI , Response
from fastapi.responses import JSONResponse
app = FastAPI()


@app.get("/items/", operation_id="some_specific_id_you_define")
async def read_items():
    return [{"item_id": "Foo"}]

'''
response cookies
cookie-and-object
'''
@app.post("/cookie-and-object")
async def create_cookie(response : Response):
    response.set_cookie(key="fakesession" , value="fake-cookie-session-value")
    return {"message"  : " i have cookies"}
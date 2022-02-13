from fastapi import FastAPI , Response , Depends
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


'''
response Headers
get_headers
'''
@app.get("/headers-and-objects")
async def get_headers(response:  Response):
    response.headers["X-Cat-dog"] ="hi"
    return {"message": "Hello World"}


'''
Advanced Dependencies
''' 
class FixedContentQueryChecker:
    def __init__(self , fixed_content :str) -> None:
        self.fixed_content = fixed_content
    
    def __call__(self, q: str = "bar") -> False:
        if q:
            return self.fixed_content in q

checker = FixedContentQueryChecker("bar")

@app.get('/query-checker')
async def read_query_check(fixed_content_included : bool = Depends(checker)):
    return {"fixed_content_in_query" : fixed_content_included}


'''
OAuth2  scopes
'''
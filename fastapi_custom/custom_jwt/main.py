from fastapi import FastAPI ,middleware ,Request  , HTTPException ,status
from starlette.responses import JSONResponse, Response

from auth import decode_and_validate_token
from todo_router import router

app = FastAPI(debug = True)
app.include_router(router)

@app.middleware("http")
async def access_db_middleware(request:Request , call_next):
    if request.url.path in ["/docs"]:
        return await call_next(request)

    bearer_token = request.headers.get("Authorization")
    if not bearer_token:
        #raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
        return JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content={
                    "detail": "Missing access token",
                    "body": "Missing access token",
                },
            )
    try :
        auth_token = bearer_token.split(" ")[1].strip()
        token_payload = decode_and_validate_token(auth_token)
    except:
        return JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content={
                    "detail": "Missing access token",
                    "body": "Missing access token",
                },
            )
    else:
        request.state.user_id = token_payload["sub"]
    return await call_next(request)
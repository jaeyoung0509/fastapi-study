from fastapi import HTTPException , status , Depends
from jose import JWTError, jwt
from datetime import datetime , timedelta
from fastapi.security import OAuth2PasswordBearer  , OAuth2PasswordRequestForm
from jose.constants import Algorithms
from sqlalchemy.sql.functions import user
from .Schemas import TokenData
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"

ouath2_scheme =  OAuth2PasswordBearer(tokenUrl="login")



def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(token :str = Depends(ouath2_scheme)):
    creentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="could not validate credentials" , 
        headers= {"WWW-Authenticate": "Bearer"},
    )
    try:
        payload  = jwt.decode(token , SECRET_KEY , algorithms=[Algorithms])
        username: str=payload.get("sub")
        if username is None:
            raise creentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise creentials_exception

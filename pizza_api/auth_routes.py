import imp
from os import access
from fastapi import APIRouter, Depends , HTTPException , status
from tortoise import json
from database import engine, Session
from schemas import SignupModel , LoginModel
from models import User
from passlib.context import CryptContext
from fastapi_jwt_auth import AuthJWT
from fastapi.encoders import jsonable_encoder


pwd_context = CryptContext(schemes=["bcrypt"] , deprecated = "auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

auth_router = APIRouter(
    prefix='/auth',
    tags= ['auth']
)

session = Session(bind = engine)


@auth_router.get('/' )
async def hello(Authorize : AuthJWT = Depends()):
    try:
        Authorize.jwt_required()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
            detail= "Invalid token ")
    return {"message" :"hello world"}

@auth_router.post('/signup' ,status_code= status.HTTP_201_CREATED)
async def signup(user: SignupModel):
    db_email = session.query(User).filter(User.email == user.email).first()
    db_username = session.query(User).filter(User.username == user.username).first()
    if db_email is not None or db_username is not None:
        return HTTPException(status_code= status.HTTP_400_BAD_REQUEST,
            detail="User wih the email already exists"
        )
    new_user =User(
        username = user.username ,
        email = user.email,
        password = get_password_hash(user.password) ,
        is_active = user.is_active , 
        is_staff = user.is_staff 
    )
    session.add(new_user)
    session.commit()

@auth_router.post('/login' , status_code= status.HTTP_200_OK)
async def login(user:LoginModel , Authorize:AuthJWT=Depends()):
    db_user = session.query(User).filter(User.username == user.username).first()
    if db_user and verify_password( user.password , db_user.password):
        access_token = Authorize.create_access_token(subject=db_user.username)
        refresh_token = Authorize.create_refresh_token(subject=db_user.username)

        response = {
            "access" : access_token ,
            "refresh" : refresh_token
        }
        return jsonable_encoder(response)
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
        detail= "Invalid Username or password  "
    )

@auth_router.get('/refresh')
async def refresh_token(Authorize : AuthJWT = Depends()):
    try:
        Authorize.jwt_refresh_token_required()
    except Exception as e:
        raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED ,
        detail="Please provide a valid refresh token")
    current_user = Authorize.get_jwt_subject()
    access_token = Authorize.create_refresh_token(subject=current_user)
    return jsonable_encoder({"access" : access_token})
from fastapi import APIRouter , HTTPException , status
from database import engine, Session
from schemas import SignupModel
from models import User
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"] , deprecated = "auto")


auth_router = APIRouter(
    prefix='/auth',
    tags= ['auth']
)

session = Session(bind = engine)

@auth_router.get('/')
async def hello():
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
        password = pwd_context.hash(user.password) ,
        is_active = user.is_active , 
        is_staff = user.is_staff 
    )
    session.add(new_user)
    session.commit()

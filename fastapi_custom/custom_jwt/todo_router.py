from fastapi import APIRouter

router = APIRouter(
    prefix="/todo" ,
    tags=["todo"]
)

@router.get("/todo")
async def get_todo():   
    return{"message" : "you called get function"}

@router.get("/todo/{id}")
async def get_todo_byId(id :int):
    return {"message" : " you called get{id} function"}

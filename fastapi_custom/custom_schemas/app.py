from datetime import datetime
import uuid
from schemas import CreateTaskSchema
from server import  server
from schemas import ListTasksSchema , GetTaskSchema
from fastapi import HTTPException, status
TODO = []

@server.get('/todo' , response_model= ListTasksSchema)
async def get_tasks():
    return {
        'tasks' : TODO
    }


@server.post('/todo' , response_model= GetTaskSchema  ,  status_code= status.HTTP_201_CREATED)
async def create_task(payload : CreateTaskSchema):
    task = payload.dict()
    task['id'] = uuid.uuid4()
    task['created']  = datetime.utcnow()
    task['priority'] = task['priority'].value
    task['status'] = task['status'].value
    TODO.append(task)
    return task


@server.get('/todo/{task_id}' , response_model= GetTaskSchema)
async def get_task_byId(task_id : uuid.UUID):
    """"""
    task_result =  [t for t in TODO if t['id'] == task_id]
    if task_result != 1 :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND
        ,detail= f"the id  {task_id} is not found")
    return task_result

@server.put('/todo{task_id}' , response_model=GetTaskSchema)
async def update_task(task_id : uuid.UUID ,  payload : CreateTaskSchema):
    """"""
    pass
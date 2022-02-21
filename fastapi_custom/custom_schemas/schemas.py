from datetime import datetime
from typing import Optional , List
from uuid import UUID
from pydantic import BaseModel 
from enum import Enum

class Error(BaseModel):
    detail : Optional[str] = None

class Priority(Enum):
    low = 'low'
    medium = 'medium'
    high =  'high'

class Status(Enum):
    progress = 'progress'
    pending = 'pending'
    completed = 'completed'


class CreateTaskSchema(BaseModel):
    """"""
    priority : Optional[Priority] = 'low'
    status  : Optional[Status] = 'pending'

class GetTaskSchema(BaseModel):
    id : UUID
    created : datetime
    priority : Priority
    task : str

class ListTasksSchema(BaseModel):
    tasks: List[GetTaskSchema] 
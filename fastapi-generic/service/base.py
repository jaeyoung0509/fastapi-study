from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session

from db.base_class import Base

ModelType = TypeVar("ModelType" , bound= Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)

class CRUDBase(Generic[ModelType , CreateSchemaType , UpdateSchemaType]):
    def __init__(self , model : Type[ModelType]) -> None:
        self.model = model

    def get(self , db : Session , id : Any) -> Optional[ModelType]:
        return db.query(self.model).filter(self.model.id == id).first()

    def get_multi(self , db : Session , * , skip : int = 10 , limit : int = 100) -> List[ModelType]:
        return db.query(self.model).offset(skip).limit(limit).all()

    def create(self ,db : Session , * , obj_in : CreateSchemaType) -> ModelType:
        obj_in_data = jsonable_encoder(obj_in)
        obj_in = self.model(**obj_in_data)
        db.add(obj_in)
        db.commit()
        db.refresh(obj_in)

    def update(self ,db : Session , * , db_obj : ModelType , obj_in : Union[UpdateSchemaType , Dict[str , Any]]) -> ModelType:
        '''
        isinstance -> type check function
        Union ->  generic tpye 
        From Python 3.10 onwards, you can use | separator for union types like go kkk
        obj_in : Union[UpdateSchemaType , Dict[str , Any]
        obj_in : UpdateSchemaType | Dict[str ,Any]

        
        '''
        obj_data = jsonable_encoder(db_obj)
        if isinstance(obj_data ,dict): 
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def remove(self ,db :  Session  , * , id: int)-> ModelType:
        obj = db.query(self.mdel).get(id)
        db.delete(obj)
        db.commit()
        return obj
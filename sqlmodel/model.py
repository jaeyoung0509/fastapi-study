from sqlmodel import SQLModel , Field

class SongBase(SQLModel):
    '''
    it's only pydantic model.
    '''
    name : str
    artist : str
    

class Song(SongBase , table= True):
    id : int = Field(default=None , primary_key= True)

class SongCreate(SongBase):
    pass
class SongUpdate(SongBase):
    pass
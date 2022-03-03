from typing import List
from sqlalchemy.ext.asyncio import AsyncSession     
from fastapi import FastAPI ,Depends , status , HTTPException
from db import init_db ,get_session 
from model import Song , SongCreate ,SongUpdate

app = FastAPI() 

@app.on_event("startup")
async def on_startup():
    return {"message" : "hello"}

@app.get("/songs/{song_id}" )
async def get_song(song_id:int , session: AsyncSession = Depends(get_session)):
    song =  await session.get(Song , song_id)
    if not song :
        raise HTTPException(status_code=404)
    return song

@app.get("/songs", response_model=List[Song])
async def get_songs(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Song))
    songs = await result.scalars().all()
    return [Song(name=song.name, artist=song.artist, id=song.id) for song in songs]

@app.post("/songs" , status_code= status.HTTP_201_CREATED)
async def add_song (song : SongCreate , session : AsyncSession = Depends(get_session)):
    song = Song(name = song.name , artist= song.artist)
    session.add(song)
    await session.commit()
    await session.refresh(song)

@app.patch("/songs{song_id}" , response_model= Song )
async def update_song(song_id:int , song : SongUpdate , session : AsyncSession = Depends(get_session)):
    db_song=  await session.get(Song , song_id)
    if not db_song :
        raise HTTPException(status_code=404)
    song_data  = song.dict(exclude_unset=True)
    for key ,value in song_data.items():
        setattr(db_song ,key, value)
    session.add(db_song)
    await session.commit()
    await session.refresh(db_song)
    return db_song


@app.delete("/songs/{song_id}")
async def update_song(song_id:int , song : SongUpdate , session : AsyncSession = Depends(get_session)):
    db_song=  await session.get(Song , song_id)
    if not db_song :
        raise HTTPException(status_code=404)
    await session.delete(db_song)
    await session.commit()
    return{"ok" : "true"}
@app.get("/ping")
async def pong():
    return {"ping" : "pong"}
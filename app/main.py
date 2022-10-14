from msilib import schema
from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from starlette.middleware.cors import CORSMiddleware

import cruds, schemas
from database import get_db

app = FastAPI()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/")
def read_root():
    return {"RED IS SUS !!": "SUUS SUUUUS AMOGUUUS !!!"}



@app.get('/entries', tags=["Entries"], response_model=list[schemas.EntryGet])
async def read_entries(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    entries = cruds.get_entries(db, skip=skip, limit=limit)
    return entries

@app.get('/entries/{entry_id}', tags=["Entries"], response_model=schemas.EntryBase)
async def read_entry(entry_id: int, db: Session = Depends(get_db)):
    entry = cruds.get_entry(db, entry_id)
    return entry

@app.post("/entries", response_model=schemas.EntryBase, tags=["Entry"])
async def create_entry(entry: schemas.EntryCreate, db: Session = Depends(get_db)):
    return cruds.create_entry(db=db, entry=entry)



@app.get('/users', tags=["Users"], response_model=list[schemas.UserBase])
async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = cruds.get_users(db, skip=skip, limit=limit)
    return users

@app.get('/users/{user_id}', tags=["Users"], response_model=schemas.UserBase)
async def read_user(user_id: int, db: Session = Depends(get_db)):
    user = cruds.get_user(db, user_id)
    return user



@app.get('/meteos', tags=["Meteo"], response_model=list[schemas.MeteoBase])
async def read_meteos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    meteos = cruds.get_meteos(db, skip=skip, limit=limit)
    return meteos

@app.get('/meteos/{meteo_id}', tags=["Meteo"], response_model=schemas.MeteoBase)
async def read_meteo(meteo_id: int, db: Session = Depends(get_db)):
    meteo = cruds.get_meteo(db, meteo_id)
    return meteo
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
    "http://localhost",
    "http://localhost:80",
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
    return {"Hello": "World"}


@app.get('/users', tags=["Users"], response_model=list[schemas.UserBase])
async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    artists = cruds.get_users(db, skip=skip, limit=limit)
    return artists
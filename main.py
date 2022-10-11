from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

class Users(BaseModel):
    firstname: str
    lastname: str


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/users/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
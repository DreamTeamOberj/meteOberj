from datetime import datetime
from pydantic import BaseModel
from sqlalchemy import BLOB

import models

class EntryBase(BaseModel):
    meteo: object
    user: object

    class Config:
        orm_mode = True

class EntryGet(EntryBase):
    date: datetime
    
class EntryCreate(EntryBase):
    id_user: int
    id_meteo: int


class MeteoBase(BaseModel):
    nom: str
    valeur: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    prenom: str
    nom: str
    pseudo: str
    statut: str

    class Config:
        orm_mode = True

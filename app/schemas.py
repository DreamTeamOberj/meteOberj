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
 

class EntryUpdate(EntryBase):
    pass

class EntryDelete(EntryBase):
    pass


class MeteoBase(BaseModel):
    nom: str
    valeur: int

    class Config:
        orm_mode = True


class MeteoCreate(MeteoBase):
    pass


class MeteoUpdate(MeteoBase):
    pass

class MeteoDelete(MeteoBase):
    pass


class UserBase(BaseModel):
    prenom: str
    nom: str
    statut: str

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    pass

class UserDelete(UserBase):
    pass


class UserUpdate(UserBase):
    pass
from datetime import datetime
from pydantic import BaseModel
from sqlalchemy import BLOB

import models

class EntryBase(BaseModel):
    date: datetime
    id_meteo: int
    id_user: int
    meteo: object
    user: object

    class Config:
        orm_mode = True


class EntryCreate(EntryBase):
    pass


class EntryUpdate(EntryBase):
    pass

class EntryDelete(EntryBase):
    pass


class MeteoBase(BaseModel):
    nom: str
    valeur: str

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
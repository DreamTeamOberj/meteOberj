from datetime import datetime
from pydantic import BaseModel


class EntrieBase(BaseModel):
    id_meteo: int
    id_user: int
    date: datetime

    class Config:
        orm_mode = True


class EntrieCreate(EntrieBase):
    pass


class EntrieUpdate(EntrieBase):
    pass

class EntrieDelete(EntrieBase):
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
    status: str

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    pass

class UserDelete(UserBase):
    pass


class UserUpdate(UserBase):
    pass
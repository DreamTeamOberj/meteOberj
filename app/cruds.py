from importlib.util import LazyLoader
from sqlalchemy.orm import Session, selectinload
import models, schemas
from datetime import date


# User CRUD
def get_user(db: Session, user_id: int):
    print(user_id)
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


# Meteo CRUD
def get_meteo(db: Session, meteo_id: int):
    return db.query(models.Meteo).filter(models.Meteo.id == meteo_id).first()


def get_meteos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Meteo).offset(skip).limit(limit).all()


# MU CRUD
def get_entry(db: Session, user_id: int):
    return db.query(models.Entry).filter(models.Entry.id_user == user_id).first()


def get_entries(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Entry).offset(skip).limit(limit).all()


def create_entry(db: Session, entry: schemas.EntryCreate):
    db_mu = models.Entry(id_user=entry.id_user, id_meteo=entry.id_meteo, date=date.today())
    db.add(db_mu)
    db.commit()
    db.refresh(db_mu)
    return db_mu
from sqlalchemy.orm import Session

import models, schemas
from datetime import date


# User CRUD
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


# Meteo CRUD
def get_meteo(db: Session, meteo_id: int):
    return db.query(models.Meteo).filter(models.Meteo.id == meteo_id).first()


def get_meteos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Meteo).offset(skip).limit(limit).all()


# MU CRUD
def get_entries(db: Session, user_id: int):
    return db.query(models.Entries).filter(models.Entries.id_user == user_id).first()


def get_all_entries(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Entries).offset(skip).limit(limit).all()


def create_entries(db: Session, entrie: schemas.EntrieCreate):
    db_mu = models.Entries(id_user=entrie.id_user, id_meteo=entrie.id_meteo, date=date.today())
    db.add(db_mu)
    db.commit()
    db.refresh(db_mu)
    return db_mu
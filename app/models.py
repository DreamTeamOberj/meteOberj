from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, true
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    prenom = Column(String)
    nom = Column(String)
    statut = Column(String)


class Meteo(Base):
    __tablename__ = "meteo"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String)
    image = Column(String)
    valeur = Column(Integer)
    
class Entries(Base):
    __tablename__ = "meto_users"
    id = Column(Integer, primary_key=True, index=True)
    id_meteo = Column(ForeignKey('meteo.id'))
    id_user = Column(ForeignKey('user.id'))
    date = Column(DateTime)
    
    meteo = relationship("Meteo")
    user = relationship("User")
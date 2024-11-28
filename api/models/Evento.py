from fastapi import Depends, FastAPI, HTTPException
from typing import Optional
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, Session
from sqlalchemy.ext.declarative import declarative_base

from models import DataBase

Base = declarative_base()

class Evento(Base):
    __tablename__ = "eventos"

    evento_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    titulo_evento = Column(String(80), nullable=False)
    descricao = Column(String(255), nullable=True)
    data_evento = Column(String(10), nullable=True)

class EventoBase(BaseModel):
    evento_id: int
    titulo_evento: str
    descricao: str
    data_evento: str


class EventoRequest(BaseModel):
    titulo_evento: str
    descricao: str
    data_evento: str


class EventoResponse(BaseModel):
    evento_id: Optional[int]
    titulo_evento: str
    descricao: str
    data_evento: str


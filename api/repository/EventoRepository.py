from fastapi import Depends
from sqlalchemy.orm import Session
from models.Evento import Evento
from strategy.InsertStrategy import InsertStrategy
from strategy.UpdateStrategy import UpdateStrategy
from repository.EventoContext import EventoContext

class EventoRepository:
    @staticmethod
    def get_all(db: Session):
        return db.query(Evento).all()
    
    @staticmethod
    def salvar(db: Session, evento: Evento):
        if evento.evento_id:
            strategy = UpdateStrategy()  # Se o evento já existir é utilizado a estratégia de atualização
        else:
            strategy = InsertStrategy()  # Se for um novo evento, é utilizado a estratégia de salvar novo

        context = EventoContext(strategy)
        return context.execute_strategy(db, evento)
    
    @staticmethod
    def atualizar(db: Session, evento: Evento):
        if evento.evento_id:
            db.merge(evento)
            db.commit()
            return evento
    
    @staticmethod
    def get_by_id(db: Session, id: int):
        return db.query(Evento).filter(Evento.evento_id == id).first()
    
    @staticmethod
    def deletar(db: Session, id: int):
        evento = db.query(Evento).filter(Evento.evento_id == id).first()
        if evento is not None:
            db.delete(evento)
            db.commit()
            return True
        return False

    @staticmethod
    def exists_by_id(db:Session, id: int) -> bool:
        return db.query(Evento).filter(Evento.evento_id == id).first() is not None

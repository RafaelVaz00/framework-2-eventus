from models.Evento import Evento
from sqlalchemy.orm import Session
from strategy.SaveStrategy import SaveStrategy

class InsertStrategy(SaveStrategy):
    def save(self, db: Session, evento: Evento):
        db.add(evento)
        db.commit()
        return evento
from models.Evento import Evento
from sqlalchemy.orm import Session
from strategy.SaveStrategy import SaveStrategy

class UpdateStrategy(SaveStrategy):
    def save(self, db: Session, evento: Evento):
        db.merge(evento)
        db.commit()
        return evento
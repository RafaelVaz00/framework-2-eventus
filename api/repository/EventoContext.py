from models.Evento import Evento
from strategy.SaveStrategy import SaveStrategy
from sqlalchemy.orm import Session

class EventoContext:
    def __init__(self, strategy: SaveStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: SaveStrategy):
        self.strategy = strategy

    def execute_strategy(self, db: Session, evento: Evento):
        return self.strategy.save(db, evento)

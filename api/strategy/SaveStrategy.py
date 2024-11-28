from abc import ABC, abstractmethod
from models.Evento import Evento
from sqlalchemy.orm import Session

class SaveStrategy(ABC):
    @abstractmethod
    def save(self, db: Session, evento: Evento):
        pass

from models.Evento import Evento

class EventoFactory:
    @staticmethod
    def create_evento(titulo_evento: str, descricao: str, data_evento: str) -> Evento:
        return Evento(
            titulo_evento=titulo_evento,
            descricao=descricao,
            data_evento=data_evento
        )

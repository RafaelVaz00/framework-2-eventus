from typing import List
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session
from models.DataBase import get_connection
from models.Evento import EventoBase
from models import Evento
import uvicorn
from models.Evento import Evento, EventoBase, EventoRequest, EventoResponse
from models.DataBase import Base, engine, get_connection
from repository.EventoRepository import EventoRepository
from factory.EventoFactory import EventoFactory



Base.metadata.create_all(bind=engine)
app = FastAPI()

origins = [
    "http://127.0.0.1:5500",  # Permitir o frontend local
    "http://localhost:5500"   # Alternativa para localhost
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "A Aplicação foi iniciada!"}

if __name__ == "__main__":
    
    uvicorn.run(app, host="127.0.0.1", port=8000)


@app.get("/eventos/todos", response_model=list[EventoBase])
async def retorna_todos_eventos(db: Session = Depends(get_connection)):
    return EventoRepository.get_all(db)

@app.post("/eventos/", response_model=EventoResponse)
async def create_evento(request: EventoRequest, db: Session = Depends(get_connection)):
    evento = EventoFactory.create_evento(
        titulo_evento=request.titulo_evento,
        descricao=request.descricao,
        data_evento=request.data_evento
    )
    
    return EventoRepository.salvar(db, evento)


@app.get("/eventos/{evento_id}", response_model=EventoResponse)
async def obter_evento_por_id(evento_id: int, db: Session = Depends(get_connection)):
    
    evento = EventoRepository.get_by_id(db, evento_id)
    
    if evento is None:
        raise HTTPException(status_code=404, detail="O Evento não foi encontrado ou não existe!")
    return evento

@app.delete("/evento/{evento_id}",status_code=status.HTTP_204_NO_CONTENT)
def deletar_evento(evento_id: int, db:Session = Depends(get_connection)):
    if not EventoRepository.exists_by_id(db, evento_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Evento não encontrado.')
    if EventoRepository.deletar(db, evento_id):
        raise HTTPException(status_code=status.HTTP_200_OK, detail='Evento deletado com sucesso!')
    else:
        raise HTTPException(status_code=status.HTTP_200_OK, detail='Não foi possível deletar o Evento.')

@app.put("/eventos/{evento_id}", response_model=EventoResponse)
async def create_evento(evento_id: int, request: EventoRequest, db: Session = Depends(get_connection)):
    if not EventoRepository.exists_by_id(db, evento_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Evento não encontrado')
    
    evento = Evento(
        titulo_evento=request.titulo_evento,
        evento_id=request.evento_id,
        descricao=request.descricao,
        data_evento=request.data_evento
    )
    return EventoRepository.atualizar(db, evento)
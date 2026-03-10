from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.model.serie import SerieModel
from app.schema.serie import SerieSchema


serie = APIRouter()

@serie.post("/")
async def criar_serie(dados: SerieSchema, db: Session = Depends(get_db)):
    nova_serie = SerieModel(**dados.model_dump())
    db.add(nova_serie)
    db.commit()
    db.refresh(nova_serie)
    return nova_serie

@serie.get("/")
async def listar_series(db: Session = Depends(get_db)):
    return db.query(SerieModel).all()

@serie.delete("/deletar/{id}")
async def deletar_serie(id: int, db: Session= Depends(get_db)):
    db.query(SerieModel).filter(SerieModel.id == id).first()
    if not serie:
        return("Não foi localizado o id")
    db.delete(id)
    return("Deletado")
    
@serie.put('/update/{id}')
async def atualizar_serie(id: int, titulo: str, descricao: str, ano_lancamento: int):
    result = {'titulo': titulo, 'descrição': descricao, "Ano Lançamento": ano_lancamento}
    return result                                                                                            
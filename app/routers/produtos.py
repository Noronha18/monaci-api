# app/routers/produtos.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

# Importamos nossos "blocos de montar"
from app.database import get_db
from app.models import Produto
from app.schemas import ItemCardapioCreate, ItemCardapioResponse  # Lembra deles?

router = APIRouter(
    prefix="/produtos",
    tags=["Produtos"]
)


# ROTA 1: CRIAR PRODUTO (POST)
@router.post("/", response_model=ItemCardapioResponse, status_code=status.HTTP_201_CREATED)
def criar_produto(produto: ItemCardapioCreate, db: Session = Depends(get_db)):
    """
    Cadastra um novo prato no cardápio.
    """
    # 1. Converter Schema (Pydantic) para Model (SQLAlchemy)
    novo_produto = Produto(
        nome=produto.nome,
        preco_atual=produto.preco,  # Agora sim: Coluna do Banco = Valor do Schema
        categoria=produto.categoria,
        descricao=produto.descricao
    )

    # 2. Salvar no Banco
    db.add(novo_produto)
    db.commit()
    db.refresh(novo_produto)  # Recarrega para pegar o ID gerado

    return novo_produto


# ROTA 2: LISTAR PRODUTOS (GET)
@router.get("/", response_model=List[ItemCardapioResponse])
def listar_produtos(db: Session = Depends(get_db)):
    return db.query(Produto).all()

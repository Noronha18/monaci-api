from pydantic import BaseModel, Field, PositiveFloat, ConfigDict
from typing import Optional


class ItemCardapioBase(BaseModel):
    nome: str = Field(..., min_length=2, description="Nome do prato")
    descricao: Optional[str] = None
    preco: PositiveFloat = Field(..., description="Preco deve ser maior que zero")
    categoria: str #Bebida, Prato principal

        # Configuracao interna para documentacao automatica

class ItemCardapioCreate(ItemCardapioBase):
    pass

class ItemCardapioResponse(BaseModel):
    id: int
    nome: str
    descricao: Optional[str] = None
    preco_atual: float
    categoria: str

# Use isto (Moderno - V2):
model_config = ConfigDict(from_attributes=True)

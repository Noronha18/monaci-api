from pydantic import BaseModel, Field, PositiveFloat, ConfigDict
from typing import Optional
from datetime import datetime

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

class ItemPedidoCreate(BaseModel):
    produto_id: int
    quantidade: int = Field(..., gt=0, example=1)


class PedidoCreate(BaseModel):
    itens: list[ItemPedidoCreate]

class ItemPedidoResponse(BaseModel):
    produto_id: int
    quantidade: int
    preco_unitario_snapshot: float

    model_config = ConfigDict(from_attributes=True)

class PedidoResponse(BaseModel):
    id: int
    status: str
    data_criacao: datetime
    itens: list[ItemPedidoResponse]

    model_config = ConfigDict(from_attributes=True)


from enum import Enum

class StatusPedido(str, Enum):
    CRIADO = "CRIADO"
    PAGO = "PAGO"
    PREPARANDO = "PREPARANDO"
    PRONTO = "PRONTO"
    ENTREGUE = "ENTREGUE"
    CANCELADO = "CANCELADO"

class PedidoUpdate(BaseModel):
    status: StatusPedido

class WebhookPagamentoMock(BaseModel):
    pedido_id: int
    status_transacao: str
    id_transacao_gateway: str
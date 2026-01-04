from fastapi import Depends, HTTPException, APIRouter, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Pedido, ItemPedido, Produto
from app.schemas import PedidoCreate, PedidoResponse, PedidoUpdate, StatusPedido

router = APIRouter(
    prefix="/pedidos",
    tags=["Pedidos"],
)

@router.post("/", response_model=PedidoResponse, status_code=status.HTTP_201_CREATED)
def criar_pedido(pedido_in: PedidoCreate, db: Session = Depends(get_db)):
    """
     Recebe uma lista de itens, valida se existem, pega o preço atual e cria o pedido.
     """

    novo_pedido = Pedido(status="CRIADO")
    db.add(novo_pedido)
    db.flush()

    lista_itens_db = []

    for item_in in pedido_in.itens:
        produto_db = db.query(Produto).filter(Produto.id == item_in.produto_id).first()

        if not produto_db:
            raise HTTPException(
                status_code=404,
                detail=f"Produto com ID {item_in.produto_id} nao encontrado."
            )

        novo_item = ItemPedido(
            pedido_id=novo_pedido.id,
            produto_id=produto_db.id,
            quantidade=item_in.quantidade,
            preco_unitario_snapshot=produto_db.preco_atual
        )

        db.add(novo_item)
        lista_itens_db.append(novo_item)

    db.commit()
    db.refresh(novo_pedido)
    return novo_pedido

@router.patch("/{pedido_id}", response_model=PedidoResponse)
def atualizar_status_pedido(pedido_id: int, atualizacao: PedidoUpdate, db: Session = Depends(get_db)):

    pedido = db.query(Pedido).filter(Pedido.id == pedido_id).first()

    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido nao encontrado")

    if pedido.status == StatusPedido.ENTREGUE and atualizacao.status == StatusPedido.CANCELADO:
        raise HTTPException(status_code=400, detail="Não é possível cancelar pedido já entregue")

    pedido.status = atualizacao.status
    db.commit()
    db.refresh(pedido)

    return pedido
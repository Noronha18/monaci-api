from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Pedido
from app.schemas import WebhookPagamentoMock, StatusPedido

router = APIRouter(
    prefix="/webhooks",
    tags=["Webhooks (Integracao)"],
)

@router.post ("/pagamento-simulado", status_code=status.HTTP_200_OK)
def receber_webhook_pagamento(
        webhook_data: WebhookPagamentoMock,
        db: Session = Depends(get_db)
):
    """
    Simula o recebimento de um Webhook de pagamento.
    Se 'status_transacao' for 'aprovado', move o pedido para PAGO.
    """
    print(f"📡 Webhook recebido: {webhook_data}") # Log simples para debug)

    pedido = db.query(Pedido).filter(Pedido.id == webhook_data.pedido_id).first()

    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido não encontrado para este pagamento")
    if pedido.status == StatusPedido.PAGO:
        return  {"msg": "Webhook processado anteriormente (Idempotência garantida)."}
    elif webhook_data.status_transacao.lower() == "aprovado":
        pedido.status = StatusPedido.PAGO
        db.commit()
        db.refresh(pedido)
        return {"msg": f"Pedido {pedido.id} atualizado para PAGO com sucesso via Webhook."}
    elif webhook_data.status_transacao.lower() == "recusado":
        # Poderíamos ter um status CANCELADO ou PAGAMENTO_FALHOU
        return {"msg": "Pagamento recusado pelo gateway. Status do pedido inalterado."}
    else:
        raise HTTPException(status_code=400, detail="Status de transacao desconhecido")
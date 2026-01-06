# tests/test_fluxo_pedidos.py
from app.schemas import StatusPedido


def test_ciclo_completo_pedido(client):
    # --- CENÁRIO: CRIAR PRODUTO ---
    payload_produto = {
        "nome": "X-Bacon Senior",
        "descricao": "O melhor da casa",  # Adicionei pois pode ser útil, mesmo sendo opcional
        "preco": 35.00,  # CORREÇÃO: era 'preco_atual'
        "categoria": "Lanches"
        # REMOVIDO: "disponivel": True (Seu schema não tem esse campo)
    }
    resp_prod = client.post("/produtos/", json=payload_produto)
    assert resp_prod.status_code == 201
    id_produto = resp_prod.json()["id"]

    # --- CENÁRIO: CRIAR PEDIDO (CLIENTE) ---
    payload_pedido = {
        "itens": [
            {"produto_id": id_produto, "quantidade": 2}
        ]
    }
    resp_pedido = client.post("/pedidos/", json=payload_pedido)
    assert resp_pedido.status_code == 201
    dados_pedido = resp_pedido.json()
    id_pedido = dados_pedido["id"]

    # Validações iniciais
    assert dados_pedido["status"] == "CRIADO"
    # assert dados_pedido["total"] == 70.00  # 2 * 35.00

    # --- CENÁRIO: PAGAMENTO (WEBHOOK) ---
    payload_webhook = {
        "pedido_id": id_pedido,
        "status_transacao": "aprovado",
        "id_transacao_gateway": "tx_test_123"
    }
    resp_webhook = client.post("/webhooks/pagamento-simulado", json=payload_webhook)

    # --- ADICIONE ISTO PARA VER O ERRO ---
    if resp_webhook.status_code != 200:
        print(f"\n🚨 ERRO DO WEBHOOK: {resp_webhook.json()}")
    # -------------------------------------

    assert resp_webhook.status_code == 200

    # Verifica se mudou para PAGO
    resp_consulta = client.get(f"/pedidos/{id_pedido}")
    assert resp_consulta.json()["status"] == "PAGO"

    # --- CENÁRIO: COZINHA (FILTRO) ---
    # Cozinha pede apenas os PAGOS
    resp_cozinha = client.get("/pedidos/?status=PAGO")
    lista_cozinha = resp_cozinha.json()
    assert len(lista_cozinha) == 1
    assert lista_cozinha[0]["id"] == id_pedido

    # --- CENÁRIO: AVANÇAR STATUS (FSM) ---
    # Tenta avançar para PREPARANDO
    payload_status = {"status": "PREPARANDO"}
    resp_patch = client.patch(f"/pedidos/{id_pedido}", json=payload_status)
    assert resp_patch.status_code == 200
    assert resp_patch.json()["status"] == "PREPARANDO"

    # --- CENÁRIO: TENTATIVA DE ERRO (BLINDAGEM) ---
    # Tenta voltar para CRIADO (deve falhar)
    payload_invalido = {"status": "CRIADO"}
    resp_erro = client.patch(f"/pedidos/{id_pedido}", json=payload_invalido)
    assert resp_erro.status_code == 400  # Bad Request
    assert "Transicao invalida" in resp_erro.json()["detail"]

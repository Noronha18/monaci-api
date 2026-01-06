# 🍔 Monaci 1.0 - Sistema de Gestão para Restaurantes

Backend robusto desenvolvido com **FastAPI** e **Clean Architecture**, focado em integridade transacional e escalabilidade.

## 🚀 Tecnologias

- **Linguagem:** Python 3.12+
- **Framework:** FastAPI
- **Banco de Dados:** PostgreSQL (via Docker)
- **ORM:** SQLAlchemy
- **Validação:** Pydantic V2
- **Testes:** Pytest (Integração/E2E)

## ⚙️ Funcionalidades Chave

- **Máquina de Estados (FSM):** Controle rígido de status do pedido (CRIADO -> PAGO -> PREPARANDO -> PRONTO).
- **Webhooks Idempotentes:** Simulação de pagamento externo com garantia contra duplicidade.
- **Transações Atômicas:** Snapshots de preço no momento do pedido (proteção contra inflação/alteração de cardápio).
- **Monitor KDS:** Filtros eficientes para visualização da cozinha.

## 🛠️ Como Rodar

1. **Subir Infraestrutura:**
   ```bash
   docker start pg-restaurante

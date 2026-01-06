🍔 Monaci Delivery API
API REST de Alta Performance para Gestão de Restaurantes e Delivery
Desenvolvido com FastAPI, PostgreSQL e Docker.

O Monaci Delivery API é um backend robusto projetado para gerenciar o ciclo de vida completo de pedidos de um restaurante, desde o cardápio até a entrega final.

Diferente de um CRUD simples, este projeto foca em Engenharia de Software e Robustez, implementando padrões de projeto avançados para garantir consistência de dados, processamento de pagamentos seguro e escalabilidade via containerização.

🏛️ Destaques da Arquitetura
⚡ FastAPI Async: Construído sobre o Starlette/Pydantic para altíssima performance e validação de dados automática.

🔄 Máquina de Estados (FSM): Controle rígido do fluxo de pedidos (CRIADO → PAGO → PREPARANDO → PRONTO → ENTREGUE). A API impede transições ilegais (ex: um pedido não pode ir de CRIADO direto para ENTREGUE sem pagamento).

🛡️ Webhooks & Idempotência: Sistema preparado para receber confirmações de pagamento externas com garantia de idempotência (processa a mesma notificação apenas uma vez, evitando duplicidade financeira).

🧪 Testes Automatizados: Cobertura de testes de integração via Pytest, garantindo que as rotas críticas (Checkout, Atualização de Status) funcionem sob estresse.

🐳 Docker Native: Infraestrutura completa (App + Banco de Dados) orquestrada via Docker Compose.

🛠️ Tech Stack
Linguagem: Python 3.12

Framework: FastAPI

Banco de Dados: PostgreSQL (via Docker)

ORM: SQLAlchemy (Async/Sync Session management)

Validação: Pydantic V2

Testes: Pytest & Requests

Infraestrutura: Docker & Docker Compose

🚀 Funcionalidades da API
1. Gestão de Cardápio (Produtos)
Cadastro, Listagem e Edição de produtos.

Controle de categorias e preços.

2. Ciclo de Pedidos (Order Lifecycle)
Checkout: Criação de pedidos com validação de itens.

Processamento: Atualização de status via transições seguras.

Pagamento: Simulação de Gateway de Pagamento via Webhook.

🔧 Como Rodar o Projeto
Opção A: Via Docker (Recomendado)
A forma mais rápida de subir o ambiente completo (API + Banco).

bash
# 1. Clone o repositório
git clone https://github.com/Noronha18/monaci-api.git
cd monaci-api

# 2. Suba os containers
docker-compose up --build
A API estará disponível em: http://localhost:8000

Opção B: Rodar Localmente (Desenvolvimento)
bash
# Crie e ative o ambiente virtual
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# .venv\Scripts\activate   # Windows

# Instale as dependências
pip install -r requirements.txt

# Suba o banco de dados (exige Postgres local rodando)
# Configure o arquivo .env com suas credenciais
python src/init_db.py

# Rode o servidor
uvicorn src.main:app --reload
📚 Documentação Interativa
O projeto conta com documentação automática via Swagger UI.
Após rodar a aplicação, acesse:

👉 http://127.0.0.1:8000/docs

✅ Status do Projeto
 Configuração de Ambiente (Docker/Linter)

 Modelagem de Dados (SQLAlchemy)

 CRUD de Produtos

 Máquina de Estados de Pedidos

 Webhook de Pagamentos

 Testes de Integração (Pytest)

Desenvolvido por Emmanuel Noronha 🥋💻
Software Engineer

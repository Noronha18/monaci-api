from app.database import engine, Base
from app.models import Produto, Pedido, ItemPedido # Importe TODOS os models aqui

# Isso é o comando mágico que cria as tabelas no Postgres
print("Criando tabelas no Banco de Dados...")
Base.metadata.create_all(bind=engine)
print("Tabelas criadas com sucesso!")

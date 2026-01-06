import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from app.database import Base, SessionLocal, engine
from app.models import Produto

def popular_banco():
    db = SessionLocal()

    if db.query(Produto).count() == 0:
        print("⚠️  O banco já contém produtos. Pulei o seed.")
        return

    print("🌱 Semeando o banco de dados...")

    cardapio = [
        Produto(nome="Monaci Burger Premium", categoria="Lanches", preco_atual=45.90),
        Produto(nome="Smash Burger Duplo", categoria="Lanches", preco_atual=28.50),
        Produto(nome="Batata Frita Rústica", categoria="Acompanhamentos", preco_atual=18.00),
        Produto(nome="Coca-Cola Zero 350ml", categoria="Bebidas", preco_atual=6.50),
        Produto(nome="Suco de Laranja Natural", categoria="Bebidas", preco_atual=12.00),
        Produto(nome="Pudim de Leite", categoria="Sobremesas", preco_atual=15.00),
    ]

    db.add_all(cardapio)
    db.commit()
    print(f"✅ Sucesso! {len(cardapio)} produtos adicionados.")
    db.close()

if __name__ == "__main__":
    popular_banco()

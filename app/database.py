from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os


# ATENÇÃO: A string de conexão do Postgres tem este formato:
# postgresql://usuario:senha@localhost:porta/nome_banco
DATABASE_URL = "postgresql://postgres:minhasenha@localhost:5433/restaurante_db"

# Para Postgres, NÃO precisamos do connect_args={"check_same_thread": False}
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

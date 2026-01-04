# main.py
from fastapi import FastAPI
from app.routers import produtos, pedidos

app = FastAPI(title="Restaurante API Sênior")

# Aqui conectamos o plugue na tomada
app.include_router(produtos.router)
app.include_router(pedidos.router)
@app.get("/")
def health_check():
    return {"status": "ok", "message": "API rodando na porta 8000"}

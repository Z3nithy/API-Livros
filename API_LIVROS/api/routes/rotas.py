from fastapi import APIRouter
from schemas.livros import Livro, livros

livros_router = APIRouter(prefix="/livros", tags=["Livros"])

@livros_router.get("/home")
def home():
    return {"message": "Bem-vindo à API de Livros!"}

@livros_router.get("/livros")
def listar_livros():
    return livros

@livros_router.get("/Consultar_livros")
def consultar_livro(id: int):
    livro = next((l for l in livros if l["id"] == id), None)
    if livro:
        return Livro(**livro)
    return {"message": "Livro não encontrado!"}

@livros_router.post("/Adicionar_livros")
def adicionar_livro(livro: Livro):
    livros.append(livro.model_dump())
    return {"message": "Livro adicionado com sucesso!"}

@livros_router.put("/Atualizar_livros/{id}")
def atualizar_livro(id: int, livro: Livro):
    for i, l in enumerate(livros):
        if l["id"] == id:
            livros[i] = livro.model_dump()
            return {"message": "Livro atualizado com sucesso!"}
    return {"message": "Livro não encontrado!"}

@livros_router.delete("/Deletar_livros/{id}")
def deletar_livro(id: int):
    for i, l in enumerate(livros):
        if l["id"] == id:
            del livros[i]
            return {"message": "Livro deletado com sucesso!"}
    return {"message": "Livro não encontrado!"}
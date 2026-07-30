from pydantic import BaseModel

class Livro(BaseModel):
    id: int
    titulo: str
    autor: str

livros = [
    {"id": 1, "titulo": "O Senhor dos Anéis", "autor": "J.R.R. Tolkien"},
    {"id": 2, "titulo": "1984", "autor": "George Orwell"},
    {"id": 3, "titulo": "O Pequeno Príncipe", "autor": "Antoine de Saint-Exupéry"},
    {"id": 4, "titulo": "Dom Casmurro", "autor": "Machado de Assis"},
    {"id": 5, "titulo": "A Revolução dos Bichos", "autor": "George Orwell"}
]
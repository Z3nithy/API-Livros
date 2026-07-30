# 📚 API de Livros

Uma API REST desenvolvida com **FastAPI** para gerenciamento de livros. O projeto permite realizar operações de CRUD (Create, Read, Update e Delete), possibilitando cadastrar, consultar, atualizar e remover livros.

## Funcionalidades

- 📖 Listar todos os livros
- 🔍 Consultar um livro por ID
- ➕ Adicionar um novo livro
- ✏️ Atualizar informações de um livro
- 🗑️ Remover um livro

## 🚀 Tecnologias

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-E92063?style=for-the-badge&logo=pydantic&logoColor=white)
![Uvicorn](https://img.shields.io/badge/Uvicorn-499848?style=for-the-badge&logo=uvicorn&logoColor=white)

## Endpoints

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/livros` | Lista todos os livros |
| GET | `/livros/{id}` | Consulta um livro |
| POST | `/livros` | Adiciona um livro |
| PUT | `/livros/{id}` | Atualiza um livro |
| DELETE | `/livros/{id}` | Remove um livro |

## 👨‍💻 Autor

**Wellington Hrafnir**

Projeto desenvolvido para estudo e prática de desenvolvimento Back-End com FastAPI.

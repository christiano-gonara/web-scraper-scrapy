# API REST para consulta de livros

API construida com FastAPI para expor os dados coletados pelo crawler Scrapy e armazenados no PostgreSQL.

## Endpoints

| Metodo | Rota | Descricao |
|---|---|---|
| GET | `/livros` | Retorna todos os livros |
| GET | `/livros/{id}` | Retorna um livro pelo ID |
| GET | `/livros/rating/{rating}` | Filtra por avaliacao (`Four` ou `Five`) |

## Como executar

### 1. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 2. Configurar variaveis de ambiente

As mesmas utilizadas pelo pipeline do Scrapy:

```bash
set DB_HOST=localhost
set DB_PORT=5432
set DB_NAME=books
set DB_USER=postgres
set DB_PASSWORD=suasenha
```

### 3. Rodar o servidor

```bash
uvicorn api.main:app --reload
```

Acessar em `http://127.0.0.1:8000/docs` (Swagger UI) ou `http://127.0.0.1:8000/livros`.
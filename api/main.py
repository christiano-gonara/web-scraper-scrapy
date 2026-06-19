import os

import psycopg2
import psycopg2.extras
from fastapi import FastAPI, HTTPException


def get_db_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=os.getenv("DB_PORT", "5432"),
        dbname=os.getenv("DB_NAME", "books"),
        user=os.getenv("DB_USER", "postgres"),
        password=os.getenv("DB_PASSWORD", ""),
    )


def execute_query(query, params=None, fetch_one=False):
    try:
        conn = get_db_connection()
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
            cur.execute(query, params)
            if fetch_one:
                return cur.fetchone()
            return cur.fetchall()
    except psycopg2.OperationalError as e:
        raise HTTPException(
            status_code=503,
            detail=f"Banco de dados indisponivel: {e}",
        )
    finally:
        if "conn" in locals():
            conn.close()


app = FastAPI(title="Books API")


@app.get("/livros")
def listar_livros():
    livros = execute_query("SELECT id, title, price, rating, availability FROM books ORDER BY id")
    return livros


@app.get("/livros/{id}")
def obter_livro(id: int):
    livro = execute_query(
        "SELECT id, title, price, rating, availability FROM books WHERE id = %s",
        (id,),
        fetch_one=True,
    )
    if livro is None:
        raise HTTPException(status_code=404, detail="Livro nao encontrado")
    return livro


@app.get("/livros/rating/{rating}")
def listar_livros_por_rating(rating: str):
    if rating not in ("Four", "Five"):
        raise HTTPException(status_code=400, detail="Rating deve ser Four ou Five")
    livros = execute_query(
        "SELECT id, title, price, rating, availability FROM books WHERE rating = %s ORDER BY id",
        (rating,),
    )
    return livros
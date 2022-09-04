from fastapi import APIRouter
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from app.connections.sqlite import SqliteConnection
from app.models.sqlite_model import SqliteModel

book_router = APIRouter()


class Book(BaseModel):
    title: str
    author: str


@book_router.post("/books")
async def insert_book(book: Book):
    with SqliteConnection() as connection:
        sqlite_model = SqliteModel(conn=connection)
        sqlite_model.create_book(title=book.title, author=book.author)

    return JSONResponse(
        status_code=200,
        content={"message": "Livro cadastrado com sucesso!", "book": book.__dict__},
    )


@book_router.get("/books")
async def get_books():
    with SqliteConnection() as connection:
        sqlite_model = SqliteModel(conn=connection)
        books = sqlite_model.get_all_books()

    return JSONResponse(status_code=200, content=[book.__dict__ for book in books])


@book_router.delete("/books/{id_book}")
async def delete_books(id_book: int):
    with SqliteConnection() as connection:
        sqlite_model = SqliteModel(conn=connection)
        sqlite_model.delete_book(id_book=id_book)

    return JSONResponse(
        status_code=200,
        content={"message": "Livro deletado com sucesso!", "id_book": id_book},
    )

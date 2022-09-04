import strawberry
from typing import List
from app.models.book import Book

from app.connections.sqlite import SqliteConnection
from app.models.sqlite_model import SqliteModel


def get_books():
    with SqliteConnection() as connection:
        books = SqliteModel(conn=connection).get_all_books()

    return books


@strawberry.type
class Query:
    books: List[Book] = strawberry.field(resolver=get_books)

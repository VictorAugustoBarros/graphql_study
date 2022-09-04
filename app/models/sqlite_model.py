from app.utils.logger import Logger
from app.models.book import Book


class SqliteModel:
    def __init__(self, conn):
        self.conn = conn
        self.cursor = self.conn.cursor()

    def create_tables(self):
        pass

    def create_book(self, title: str, author: str):
        self.cursor.execute(
            """
                INSERT INTO BOOKS (title, author) VALUES ('%s', '%s')
            """
            % (title, author)
        )
        Logger().info(
            {"message": "Sucesso ao cadastrar livro!", "title": title, "author": author}
        )

    def get_all_books(self):
        response = self.cursor.execute(
            """
                SELECT id_book, title, author FROM BOOKS
            """
        )
        rows = response.fetchall()
        books = []
        for row in rows:
            books.append(Book(id=row[0], title=row[1], author=row[2]))

        return books

    def delete_book(self, id_book: int):
        self.cursor.execute(
            """
                DELETE FROM BOOKS WHERE id_book = %s
            """
            % id_book
        )

import sqlite3


class SqliteConnection:
    def __enter__(self):
        with open("app/connections/tables.sql", "r") as sql_file:
            sql_script = sql_file.read()

        self.con = sqlite3.connect("app/connections/library.db")
        cursor = self.con.cursor()
        cursor.executescript(sql_script)

        return self.con

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.con.commit()
        self.con.close()

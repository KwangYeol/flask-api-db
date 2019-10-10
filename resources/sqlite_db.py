import sqlite3
from sqlite3 import Error


class Sqlite:
    def __init__(self):
        self.app = None
        self.conn = None
        self.db_file = None

    def init_app(self, app):
        print(">>>>>>>>> Sqlite.init_app <<<<<<<<<")
        self.app = app
        self.db_file = self.app.config["SQLITE_DB_FILE"]
        self.connect()

    def connect(self):
        print(">>>>>>>>> Sqlite.connect <<<<<<<<<")
        try:
            self.conn = sqlite3.connect(self.db_file)
            print(sqlite3.version)
        except Error as e:
            print(e)

    def close(self):
        if self.conn:
            self.conn.close()
        self.conn = None

    def get_db(self):
        print(">>>>>>>>> Sqlite.get_db <<<<<<<<<")
        if not self.conn:
            return self.connect()
        return self.conn

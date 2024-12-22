import sqlite3

class DatabaseManager:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()

    def create_table(self, create_table_sql):
        self.cursor.execute(create_table_sql)

    def insert_data(self, insert_sql, data):
        self.cursor.executemany(insert_sql, data)

    def insert_single_record(self, insert_sql, record):
        self.cursor.execute(insert_sql, record)

    def commit(self):
        self.connection.commit()

    def close(self):
        self.connection.close()
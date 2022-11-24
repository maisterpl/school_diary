import sqlite3

class Database:
    def __init__(self, database_name) -> None:
        self.connection = sqlite3.connect(database_name)
        self.cursor = self.connection.cursor()
        
    def __def__(self):
        self.connection.close()
        
    def create_table(self, sql: str):
        self.cursor.execute(sql)
        self.connection.commit()
        
    def insert(self, table, *values):
        # print(f"INSERT INTO { table } VALUES ({ ','.join(['?' for _ in values]) })")
        self.cursor.execute(f"INSERT OR IGNORE INTO { table } VALUES ( { ','.join(['?' for _ in values]) } )", values)
        self.connection.commit()

    def insert_students_to_class(self, table, values):
        # print(f"INSERT INTO { table } VALUES ({ ','.join(['?' for _ in values]) })")
        self.cursor.execute(f"""INSERT OR IGNORE INTO { table } VALUES ( { ','.join(['?' for _ in values]) } )""", values)
        self.connection.commit()
        
    def fetch_all(self, table, **conditions):
        # "SELECT * FROM urls WHERE category=?", category
        # "SELECT * FROM urls where first_name AND last_name", (first_name, last_name)
        return self.cursor.execute(
            f"SELECT * FROM { table } WHERE { ' and '.join([f'{ condition }=?' for condition in conditions]) }",
            list(conditions.values())
        )
        
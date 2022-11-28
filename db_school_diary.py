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
        self.cursor.execute(f"""INSERT OR IGNORE INTO { table }
                                (id, student_name, student_subname, student_pesel)
                                VALUES ( { ','.join(['?' for _ in values]) } )""", values)
        self.connection.commit()

    def alter_table_add_new_column_to_table(self, table, lesson):
        try:
            self.cursor.execute(f"""ALTER TABLE { table } ADD COLUMN 
                                    { lesson } TEXT
            """)
            self.connection.commit()
        except:
            pass

    def update_students_assessments(self, table, pesel, lesson, assessments):
        try:
            tuple_assessments = (','.join([str(x) for x in assessments]))
            tuple_to_db = []
            tuple_to_db.append(tuple_assessments)
            self.cursor.execute(f"update { table } set { lesson }=? WHERE student_pesel={ pesel }", tuple_to_db)
            self.connection.commit()
        except sqlite3.Error as error:
            print("Failed to update rows of sqlite table: ", error)
        
    def fetch_all(self, table, **conditions):
        # "SELECT * FROM urls WHERE category=?", category
        # "SELECT * FROM urls where first_name AND last_name", (first_name, last_name)
        return self.cursor.execute(
            f"SELECT * FROM { table } WHERE { ' and '.join([f'{ condition }=?' for condition in conditions]) }",
            list(conditions.values())
        )
        
from School import Teacher, Class, Lesson, Student, School
from db_school_diary import Database



class School_to_database:
    def __init__(self, database_name, class_school_name: School) -> None:
        self.database_name = database_name
        self.database = Database(database_name)
        self.class_school_name = class_school_name
        self.school_name = self.class_school_name.name_of_school
        print(self.school_name)

    # def create_school_and_db(self):
        self.database.create_table(f'''CREATE TABLE IF NOT EXISTS test_name
                    (   id INTEGER PRIMARY KEY AUTOINCREMENT,
                        classes TEXT )
                        ''')
        self.database.insert(self.class_school_name, self.class_school_name.get_all_classes_name())
        
        for class_s in self.class_school_name.ALL_CLASS:
            self.database.create_table(f'''CREATE TABLE IF NOT EXISTS { class_s.name_of_class }
                    (   id INTEGER PRIMARY KEY AUTOINCREMENT,
                        student_name TEXT,
                        student_subname TEXT,
                        student_pesel INTEGER)
                        ''')
            self.database.insert(class_s.name_of_class, None, class_s.get_all_students_from_class())
        
    


# school_to_database = School_to_database('school_in_database.db', school_name=)
    
    




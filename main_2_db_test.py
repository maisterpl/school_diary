from School import Teacher, Class, Lesson, Student, School
from db_school_diary import Database



class School_to_database:
    def __init__(self, database_name, class_school_name: School) -> None:
        self.database_name = database_name
        self.database = Database(database_name)
        self.class_school_name = class_school_name
        self.school_name = self.class_school_name.name_of_school.replace(' ', '_')
        print(self.school_name)

    # def create_school_and_db(self):
        self.database.create_table(f'''CREATE TABLE IF NOT EXISTS { self.school_name }
                    (   id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                        classes TEXT UNIQUE)
                        ''')

        # class name add to database
        for class_name in self.class_school_name.get_all_classes_name():
            self.database.insert(self.school_name, None, class_name)
        
        for class_s in self.class_school_name.ALL_CLASS:
            # print(f'Class adding to DB: { class_s }, { class_s.name_of_class }')
            self.database.create_table(f'''CREATE TABLE IF NOT EXISTS { class_s.name_of_class }
                    (   id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                        student_name TEXT UNIQUE,
                        student_subname TEXT UNIQUE,
                        student_pesel INTEGER UNIQUE)
                        ''')

            for student_name_subnam_and_pesel in class_s.get_all_students_from_class():
                student_name_subnam_and_pesel.insert(0, None)
                self.database.insert_students_to_class(class_s.name_of_class, student_name_subnam_and_pesel)
        
    


# school_to_database = School_to_database('school_in_database.db', school_name=)
    
    




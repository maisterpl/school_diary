from School import Teacher, Class, Lesson, Student, School
from db_school_diary import Database


class School_to_database:
    def __init__(self, database_name, class_school_name: School) -> None:
        self.database_name = database_name
        self.database = Database(database_name)
        self.class_school_name = class_school_name
        self.school_name = self.class_school_name.name_of_school.replace(' ', '_')

        # create database
        self.database.create_table(f'''CREATE TABLE IF NOT EXISTS { self.school_name }
                    (   id INTEGER PRIMARY KEY AUTOINCREMENT,
                        classes TEXT UNIQUE)
                        ''')

        # class name add to database
        for class_name in self.class_school_name.get_all_classes_name():
            self.database.insert(self.school_name, None, class_name)
        
        # students add to database
        for class_s in self.class_school_name.ALL_CLASS:
            # print(f'Class adding to DB: { class_s }, { class_s.name_of_class }')
            self.database.create_table(f'''CREATE TABLE IF NOT EXISTS { class_s.name_of_class }
                    (   id INTEGER PRIMARY KEY AUTOINCREMENT,
                        student_name TEXT,
                        student_subname TEXT,
                        student_pesel INTEGER UNIQUE)
                        ''')

            for student_name_subnam_and_pesel in class_s.get_all_students_from_class():
                student_name_subnam_and_pesel.insert(0, None)
                self.database.insert_students_to_class(class_s.name_of_class, student_name_subnam_and_pesel)

            for lesson in class_s.LESSONS:
                self.database.alter_table_add_new_column_to_table(class_s.name_of_class, lesson.get_name_of_lesson())

        # add all lessons assessments to students
        for class_s in self.class_school_name.ALL_CLASS:
            for student in class_s.STUDENTS:
                for lesson in student.SCHOOL_ASSESSMENTS.keys():
                    self.database.update_students_assessments(class_s.name_of_class, student.pesel, lesson, student.SCHOOL_ASSESSMENTS[lesson])
        
    def print_db_from_current_table(self, table):
        table = table.replace(' ', '_')
        data = self.database.fetch_all(table)
        for i in data:
            print(i)


    
    




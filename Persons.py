

class Lesson():
    ASSESSMENTS = []

    def __init__(self, name_of_lesson: str, name_of_teacher: str) -> None:
        self.name_of_lesson = name_of_lesson
        self.name_of_teacher = name_of_teacher

    def __str__(self) -> str:
        return f"{ self.name_of_lesson } teacher is { self.name_of_teacher }."

    def add_rating(self):
        pass


class Person():
    def __init__(self, name: str, subname: str, pesel: int = 0) -> None:
        self.name = name
        self.subname = subname
        self.pesel = pesel
    
    def __str__(self) -> str:
        return f"{ self.name } { self.subname }."


class Teacher(Person):
    SCHOOL_SUBJECTS_TO_WORK = []

    def add_subject_to_work(self, name_of_lesson: str):
        name_of_lesson = Lesson(name_of_lesson, self.name + " " + self.subname)
        self.SCHOOL_SUBJECTS_TO_WORK.append(name_of_lesson)


class Student(Person):
    SCHOOL_SUBJECTS_TO_LERN = []
    

class Class():
    STUDENTS = []
    TEACHERS = []

    def __init__(self, name_of_class) -> None:
        self.name_of_class = name_of_class

    def add_student(self, name: str, subname: str, pesel: int):
        self.STUDENTS.append(Student(name, subname))

    def add_techer(self, name: str, subname: str, pesel: int):
        self.STUDENTS.append(Teacher(name, subname))
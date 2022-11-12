

class Lesson():

    def __init__(self, name_of_lesson: str) -> None:
        self.name_of_lesson = name_of_lesson

    def __str__(self) -> str:
        return f"{ self.name_of_lesson } teacher is { self.name_of_teacher }."


class Person():
    def __init__(self, name: str, subname: str, pesel: int = 0) -> None:
        self.name = name
        self.subname = subname
        self.pesel = pesel
    
    def __str__(self) -> str:
        return f"{ self.name } { self.subname }."


class Teacher(Person):
    
    def __init__(self, name: str, subname: str, pesel: int = 0) -> None:
        super().__init__(name, subname, pesel)


class Student(Person):
    
    def __init__(self, name: str, subname: str, pesel: int = 0) -> None:
        super().__init__(name, subname, pesel)
        self.SCHOOL_SUBJECTS_TO_LERN = []
        self.SCHOOL_ASSESSMENTS = {}  # dict = { key: lesson = value: [ assesments ] }
    
    def add_subject_to_lern(self, name_of_lesson: str):
        if name_of_lesson not in self.SCHOOL_SUBJECTS_TO_LERN:
            self.SCHOOL_SUBJECTS_TO_LERN.append(name_of_lesson)
            self.SCHOOL_ASSESSMENTS[name_of_lesson] = []
    
    def add_assessments_to_lesson(self, name_of_lesson: str, assesment: int):
        self.SCHOOL_ASSESSMENTS[name_of_lesson].append(assesment)
    

class Class():

    def __init__(self, name_of_class: str,) -> None:
        self.name_of_class = name_of_class
        self.STUDENTS = []
        self.TEACHERS = []
        self.LESSONS = []

    def __str__(self) -> str:
        return f"Name of class: { self.name_of_class }."

    def add_student(self, name: str, subname: str, pesel: int):
        self.STUDENTS.append(Student(name, subname, pesel))

    def add_teacher(self, name: str, subname: str, pesel: int):
        self.name_of_teacher = name + subname
        self.TEACHERS.append(name_of_teacher = Teacher(name, subname, pesel))
        
    def add_lesson(self, name_of_lesson: str):
        self.LESSONS.append(name_of_lesson = Lesson(name_of_lesson))
        
    def add_subject_to_work(self, name_of_lesson: str):
        name_of_lesson = Lesson(name_of_lesson)
        self.LESSONS.append(name_of_lesson)
        
        
class School():

    def __init__(self, name_of_school: str) -> None:
        self.name_of_school = name_of_school
        self.ALL_CLASS = []
        
    def make_class(self, name_of_class: str):
        name_of_class = Class(name_of_class)
        self.ALL_CLASS.append(name_of_class)
        
    def lesson_students_and_assesment(self, name_of_lesson: str) -> dict:
        lesson_students_and_assesment = {}  # dict = { key: student = value: [assesment] }
        for i in self.ALL_CLASS:
            print(i)
            for k in i.STUDENTS:
                print(k)
                for j in k.SCHOOL_ASSESSMENTS.keys():
                    print(j)
                    if j == name_of_lesson:
                        lesson_students_and_assesment[k] = list(k.SCHOOL_ASSESSMENTS.values())[0]
        
        return lesson_students_and_assesment
        
        
        
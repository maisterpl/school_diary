

class Lesson():

    def __init__(self, name_of_lesson: str) -> None:
        self.name_of_lesson = name_of_lesson

    def __str__(self) -> str:
        return f"{ self.name_of_lesson } teacher is ... ."
    
    def get_name_of_lesson(self):
        return self.name_of_lesson


class Person():
    def __init__(self, name: str, subname: str, pesel: int = 0, gender: str = '') -> None:
        self.name = name
        self.subname = subname
        self.pesel = pesel
        self.gender = gender
    
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
        lessons = [x.get_name_of_lesson() for x in self.SCHOOL_SUBJECTS_TO_LERN]
        if name_of_lesson not in lessons:
            name_of_lesson_class = Lesson(name_of_lesson)
            self.SCHOOL_SUBJECTS_TO_LERN.append(name_of_lesson_class)
            self.SCHOOL_ASSESSMENTS[name_of_lesson_class.get_name_of_lesson()] = []
    
    def add_assessments_to_lesson(self, name_of_lesson: str, assesment: int):
        self.SCHOOL_ASSESSMENTS[name_of_lesson].append(assesment)
        
    def get_assessments(self):
        return self.SCHOOL_ASSESSMENTS
    
    def get_name_of_student(self):
        return self.name + ' ' + self.subname
    

class Class():

    def __init__(self, name_of_class: str,) -> None:
        self.name_of_class = name_of_class
        self.STUDENTS = []
        self.TEACHERS = []
        self.LESSONS = []

    def __str__(self) -> str:
        return f"Name of class: \"{ self.name_of_class }\"."
    
    def get_all_students_from_class(self):
        return [ [ s.name, s.subname, s.pesel] for s in self.STUDENTS ]

    def add_student(self, name: str, subname: str, pesel: int):
        self.STUDENTS.append(Student(name, subname, pesel))

    def add_teacher(self, name: str, subname: str, pesel: int):
        self.name_of_teacher = name + '_' + subname
        self.TEACHERS.append(name_of_teacher = Teacher(name, subname, pesel))
        
    def add_lesson(self, name_of_lesson: str):
        name_of_lesson = Lesson(name_of_lesson)
        self.LESSONS.append(name_of_lesson)
        for i in self.STUDENTS:
            i.add_subject_to_lern(name_of_lesson.get_name_of_lesson())
        
    def get_student_assessments(self, pesel: int, name: str = '', subname: str = ''):
        if name == '' or subname == '':
            for i in self.STUDENTS:
                if i.pesel == pesel:
                    return i.get_assessments()
                
    def get_all_student_assessments_from_class(self):
        all_student_assessments_from_class = {}
        for i in self.STUDENTS:
            all_student_assessments_from_class[i.name + '_' + i.subname] = i.get_assessments()
        return all_student_assessments_from_class

        
class School():

    def __init__(self, name_of_school: str) -> None:
        self.name_of_school = name_of_school
        self.ALL_CLASS = []
        
    def make_class(self, name_of_class: str):
        name_of_class = Class(name_of_class)
        self.ALL_CLASS.append(name_of_class)
        
    def get_all_classes_name(self):
        return [None] + [c.name_of_class for c in self.ALL_CLASS]
        
    def add_student_to_class(self, name: str, subname: str, pesel: int, name_of_class: str = ''):
        if name_of_class == '':
            print("Chose one class from below:")
            for i in self.ALL_CLASS:
                print(i)
        else:
            for c in self.ALL_CLASS:
                if c.name_of_class == name_of_class:
                    self.ALL_CLASS[self.ALL_CLASS.index(c)].add_student(name, subname, pesel)            
        
    def lesson_students_and_assesment(self, name_of_lesson: str) -> dict:
        lesson_students_and_assesment = {}  # dict = { key: student = value: [assesment] }
        for i in self.ALL_CLASS:
            for k in i.STUDENTS:
                for j in k.SCHOOL_ASSESSMENTS.keys():
                    if j == name_of_lesson:
                        lesson_students_and_assesment[k] = list(k.SCHOOL_ASSESSMENTS.values())[0]
        return lesson_students_and_assesment
    
    def lesson_students_and_assesment_print(self, name_of_lesson_students_and_assesment_to_print: str):
        lesson_students_and_assesment_to_print = self.lesson_students_and_assesment(name_of_lesson_students_and_assesment_to_print)
        print(f"Lesson: { name_of_lesson_students_and_assesment_to_print }.")
        for i in lesson_students_and_assesment_to_print:
            print(f"{ i }: { lesson_students_and_assesment_to_print.get(i) }")
            
    def print_all_students(self):
        for i in self.ALL_CLASS:
            for j in i.STUDENTS:
                print(j)
                
    def get_all_students_which_lern_lesson(self, name_of_lesson: str):
        students_which_lern_lesson = {}  # key: student = value: assessments
        for i in self.ALL_CLASS:
            for k in i.STUDENTS:
                if name_of_lesson in [ x.get_name_of_lesson() for x in k.SCHOOL_SUBJECTS_TO_LERN ]:
                    students_which_lern_lesson[k.get_name_of_student()] = k.SCHOOL_ASSESSMENTS[name_of_lesson]
        return students_which_lern_lesson
        
        
        
from Persons import Teacher, Class, Lesson, Student, School

teacher = Teacher("Krzysztof", "Kotowicz")

print(teacher)
print()

# here made class School and class in school and print class's name
school_one = School(name_of_school="school one")
school_one.make_class(name_of_class="class_1B")
print(school_one.ALL_CLASS[0])

# here made in class 1B new student and printed it 
school_one.ALL_CLASS[0].add_student(name="Maciej", subname="Krzysztof", pesel=89110500235)
print(school_one.ALL_CLASS[0].STUDENTS[0])

school_one.ALL_CLASS[0].STUDENTS[0].add_subject_to_lern("Math")
school_one.ALL_CLASS[0].STUDENTS[0].add_assessments_to_lesson("Math", 5)
school_one.ALL_CLASS[0].STUDENTS[0].add_assessments_to_lesson("Math", 1)
print(school_one.ALL_CLASS[0].STUDENTS[0].SCHOOL_ASSESSMENTS)

# here made class School and class in school and print class's name
school_one.make_class(name_of_class="class_1A")
print(school_one.ALL_CLASS[1])

# here made in class 1A new student and printed it 
school_one.ALL_CLASS[1].add_student("Krzysztof", "Tiger", 91020200677)
print(school_one.ALL_CLASS[1].STUDENTS[0])

# here made in class 1A new student and printed it and add to it lessons 
# and assessments
school_one.ALL_CLASS[1].STUDENTS[0].add_subject_to_lern("Math")
print(school_one.ALL_CLASS[1].STUDENTS[0].SCHOOL_SUBJECTS_TO_LERN[0])
school_one.ALL_CLASS[1].STUDENTS[0].add_assessments_to_lesson("Math", 4)
school_one.ALL_CLASS[1].STUDENTS[0].add_assessments_to_lesson("Math", 3)
school_one.ALL_CLASS[1].STUDENTS[0].add_subject_to_lern("Math")
school_one.ALL_CLASS[1].STUDENTS[0].add_assessments_to_lesson("Math", 1)
school_one.ALL_CLASS[1].STUDENTS[0].add_subject_to_lern("Math")
print(school_one.ALL_CLASS[1].STUDENTS[0].SCHOOL_SUBJECTS_TO_LERN)
print(school_one.ALL_CLASS[1].STUDENTS[0].SCHOOL_ASSESSMENTS)
print()

# here made in class 1A new student and printed it and add to it lessons 
# and assessments
school_one.ALL_CLASS[1].add_student("Marcin", "Najman", 88021300159)
print(school_one.ALL_CLASS[1].STUDENTS[1])
print(school_one.ALL_CLASS[1].STUDENTS[1].SCHOOL_SUBJECTS_TO_LERN)
print(school_one.ALL_CLASS[1].STUDENTS[1].SCHOOL_ASSESSMENTS)
school_one.ALL_CLASS[1].STUDENTS[1].add_subject_to_lern("Poland")
print(school_one.ALL_CLASS[1].STUDENTS[1].SCHOOL_SUBJECTS_TO_LERN)
print(school_one.ALL_CLASS[1].STUDENTS[1].SCHOOL_ASSESSMENTS)
school_one.ALL_CLASS[1].STUDENTS[1].add_assessments_to_lesson("Poland", 1)
school_one.ALL_CLASS[1].STUDENTS[1].add_assessments_to_lesson("Poland", 1)
school_one.ALL_CLASS[1].STUDENTS[1].add_assessments_to_lesson("Poland", 1)
school_one.ALL_CLASS[1].STUDENTS[1].add_subject_to_lern("Physic")
school_one.ALL_CLASS[1].STUDENTS[1].add_assessments_to_lesson("Physic", 3)
school_one.ALL_CLASS[1].STUDENTS[1].add_assessments_to_lesson("Physic", 3.5)
print(school_one.ALL_CLASS[1].STUDENTS[1].SCHOOL_SUBJECTS_TO_LERN)
print(school_one.ALL_CLASS[1].STUDENTS[1].SCHOOL_ASSESSMENTS)

print()

print("=" * 50, "\n")

# here it is test function in Shool class where we can set name lesson and
# get all students who lern with assessments
lesson_students_and_assesment_1 = school_one.lesson_students_and_assesment(name_of_lesson="Math")
print(lesson_students_and_assesment_1)

for i in lesson_students_and_assesment_1:
    print(i)
    print(lesson_students_and_assesment_1.get(i))

print("=" * 200, "\n")



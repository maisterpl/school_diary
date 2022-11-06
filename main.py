from Persons import Teacher

teacher = Teacher("Krzysztof", "Kotowicz")
teacher.add_subject_to_work("Math")

print(teacher)
print(teacher.SCHOOL_SUBJECTS_TO_WORK[0])
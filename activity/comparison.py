# add your get_student_with_more_classes function here!
from .student import Student
def get_student_with_more_classes(student1, student2):
    if student1.get_num_classes() > student2.get_num_classes():
        return student1.name
    else:
        student2.name



from statistics import mean
class Class:
    students = []
    grades = []
    __students_count = 22

    def __init__(self, name):
        self.name = name

    def add_student(self, name:str, grade:float):
        if len(Class.students) < Class.__students_count:
            Class.students.append(name)
            Class.grades.append(grade)

    def get_average_grade(self):
        return f"{mean(Class.grades):.2f}"

    def __repr__(self):
        return f"The students in {self.name}: {', '.join(Class.students)}. Average grade: {self.get_average_grade()}"


a_class = Class("11B")
a_class.add_student("Peter", 4.80)
a_class.add_student("George", 6.00)
a_class.add_student("Amy", 3.50)
print(repr(a_class))
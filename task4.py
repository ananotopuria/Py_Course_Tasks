class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def get_average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def __str__(self):
        average_grade = self.get_average_grade()
        return f"Name: {self.name}, Grades: {self.grades}, Average: {average_grade:.2f}"


class Classroom:
    def __init__(self):
        self.students = []

    def add_student(self, new_student):
        self.students.append(new_student)

    def get_top_students(self):
        return sorted(self.students, key=lambda student: student.get_average_grade(), reverse=True)[:3]

    def get_failed_students(self):
        return [student for student in self.students if student.get_average_grade() < 51]


student1 = Student("Ana")
student2 = Student("Tekla")
student3 = Student("Dato")
student4 = Student("Liana")
student1.add_grade(85)
student1.add_grade(90)
student1.add_grade(78)
student2.add_grade(65)
student2.add_grade(70)
student2.add_grade(72)
student3.add_grade(45)
student3.add_grade(50)
student3.add_grade(48)
student4.add_grade(95)
student4.add_grade(92)
student4.add_grade(98)

classroom = Classroom()
classroom.add_student(student1)
classroom.add_student(student2)
classroom.add_student(student3)
classroom.add_student(student4)


print("Top 3 Students:")
for student in classroom.get_top_students():
    print(student)

print("Failed Students:")
for student in classroom.get_failed_students():
    print(student)

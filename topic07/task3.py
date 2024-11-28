class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} років"

students = [
    Student("Катерина", 18),
    Student("Дмитро", 20),
    Student("Максим", 22),
    Student("Аріна", 19)
]

sortedstud = sorted(students, key=lambda student: student.age)

for student in sortedstud:
    print(student)
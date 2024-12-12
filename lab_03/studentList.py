class StudentList:
    def __init__(self):
        self.students = []

    def addStudent(self, student):
        insert_position = 0
        for i in range(len(self.students)):
            if student.name.lower() > self.students[i].name.lower():
                insert_position += 1
            else:
                break
        self.students.insert(insert_position, student)
        print("New student has been added.")

    def deleteStudent(self, name):
        delete_position = -1
        for i, student in enumerate(self.students):
            if name.lower() == student.name.lower():
                delete_position = i
                break
        if delete_position != -1:
            del self.students[delete_position]
            print(f"Student with name {name} has been deleted.")
        else:
            print(f"No student with name {name} found.")

    def updateStudent(self, name, new_name=None, phone=None, email=None, address=None):
        student = next((s for s in self.students if s.name == name), None)
        if not student:
            print("Student was not found.")
            return

        if new_name:
            student.name = new_name
        if phone:
            student.phone = phone
        if email:
            student.email = email
        if address:
            student.address = address
        print(f"Information about {name} has been updated.")

    def printAll(self):
        if not self.students:
            print("Student list is empty.")
        for student in self.students:
            print(student)

import csv
from student import Student

class FileHandler:
    def loadFromCsv(self, file_name, student_list):
        try:
            with open(file_name, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    student = Student(row['name'], row['phone'], row['email'], row['address'])
                    studentList.addStudent(student)
            print(f"Data successfully loaded from {file_name}")
        except FileNotFoundError:
            print(f"File {file_name} not found. Starting with an empty student list.")

    def saveToCsv(self, file_name, student_list):
        with open(file_name, mode='w', newline='') as file:
            fieldnames = ["name", "phone", "email", "address"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for student in studentList.students:
                writer.writerow({
                    "name": student.name,
                    "phone": student.phone,
                    "email": student.email,
                    "address": student.address
                })
        print(f"Data successfully saved to {file_name}")
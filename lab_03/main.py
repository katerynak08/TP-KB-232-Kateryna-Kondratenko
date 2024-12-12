import sys
from student import Student
from studentList import StudentList
from file import FileHandler

def main():
    studentList = StudentList()
    fileHandler = FileHandler()

    if len(sys.argv) > 1:
        fileHandler.loadFromCsv(sys.argv[1], student_list)
    
    while True:
        choice = input("Please specify the action [ C create, U update, D delete, P print, X exit ]: ")
        if choice.lower() == "c":
            name = input("Please enter student name: ")
            phone = input("Please enter student phone: ")
            email = input("Please enter student email: ")
            address = input("Please enter student address: ")
            student = Student(name, phone, email, address)
            studentList.addStudent(student)
        elif choice.lower() == "u":
            name = input("Please enter the name of the student to be updated: ")
            new_name = input("Enter new name (leave blank to keep current): ") or None
            phone = input("Enter new phone (leave blank to keep current): ") or None
            email = input("Enter new email (leave blank to keep current): ") or None
            address = input("Enter new address (leave blank to keep current): ") or None
            studentList.updateStudent(name, new_name, phone, email, address)
        elif choice.lower() == "d":
            name = input("Please enter name to be deleted: ")
            studentList.deleteStudent(name)
        elif choice.lower() == "p":
            studentList.printAll()
        elif choice.lower() == "x":
            if len(sys.argv) > 1:
                fileHandler.saveToCsv(sys.argv[1], student_list)
            print("Exit()")
            break
        else:
            print("Wrong choice")

if __name__ == "__main__":
    main()

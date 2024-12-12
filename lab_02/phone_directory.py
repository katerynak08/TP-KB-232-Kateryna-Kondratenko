import csv
import sys

directory = []

def loadFromCsv(file_name):
    global directory
    try:
        with open(file_name, mode='r') as file:
            reader = csv.DictReader(file)
            directory = [row for row in reader]
        print(f"Data successfully loaded from {file_name}")
    except FileNotFoundError:
        print(f"File {file_name} not found. Starting with an empty directory.")
    return

def saveToCsv(file_name):
    global directory
    with open(file_name, mode='w', newline='') as file:
        fieldnames = ["name", "phone", "email", "address"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(directory)
    print(f"Data successfully saved to {file_name}")
    return

def printAllList():
    if not directory:
        print("Directory is empty.")
    for elem in directory:
        strForPrint = f"Student name: {elem['name']}, Phone: {elem['phone']}, Email: {elem['email']}, Address: {elem['address']}"
        print(strForPrint)
    return

def addNewElement(name=None, phone=None, email=None, address=None):
    if name is None:
        name = input("Please enter student name: ")
    if phone is None:
        phone = input("Please enter student phone: ")
    if email is None:
        email = input("Please enter student email: ")
    if address is None:
        address = input("Please enter student address: ")

    newItem = {"name": name, "phone": phone, "email": email, "address": address}

    insertPosition = 0
    for item in directory:
        if name.lower() > item["name"].lower():
            insertPosition += 1
        else:
            break
    directory.insert(insertPosition, newItem)
    print("New element has been added.")
    return

def deleteElementByName(name):
    deletePosition = -1
    for item in directory:
        if name.lower() == item["name"].lower():
            deletePosition = directory.index(item)
            break
    if deletePosition != -1:
        del directory[deletePosition]
        print(f"Element with name {name} has been deleted.")
    else:
        print(f"No element with name {name} found.")
    return

def updateElement():
    name = input("Please enter the name of the student to be updated: ")
    student = next((item for item in directory if item["name"] == name), None)
    
    if not student:
        print("Element was not found.")
        return

    print("Leave the field blank if you don't want to update it.")
    new_name = input(f"Enter new name (current: {student['name']}): ") or student['name']
    phone = input(f"Enter new phone (current: {student['phone']}): ") or student['phone']
    email = input(f"Enter new email (current: {student['email']}): ") or student['email']
    address = input(f"Enter new address (current: {student['address']}): ") or student['address']

    deleteElementByName(name)
    addNewElement(new_name, phone, email, address)
    print(f"Information about {name} has been updated.")
    return

def main():
    if len(sys.argv) > 1:
        loadFromCsv(sys.argv[1])
    
    while True:
        choice = input("Please specify the action [ C create, U update, D delete, P print, X exit ]: ")
        match choice:
            case "C" | "c":
                print("New element will be created:")
                addNewElement()
                printAllList()
            case "U" | "u":
                print("Existing element will be updated:")
                updateElement()
                printAllList()
            case "D" | "d":
                print("Element will be deleted:")
                name_to_delete = input("Please enter name to be deleted: ")
                deleteElementByName(name_to_delete)
                printAllList()
            case "P" | "p":
                print("List will be printed:")
                printAllList()
            case "X" | "x":
                if len(sys.argv) > 1:
                    saveToCsv(sys.argv[1])
                print("Exit()")
                break
            case _:
                print("Wrong choice")

if __name__ == "__main__":
    main()
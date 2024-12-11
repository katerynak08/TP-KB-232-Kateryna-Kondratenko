list = [
    {"name": "Bob", "phone": "0631234567", "email": "bob@example.com", "address": "895 Street"},
    {"name": "Emma", "phone": "0631234567", "email": "emma@example.com", "address": "123 Street"},
    {"name": "Jon", "phone": "0631234567", "email": "jon@example.com", "address": "27 Street"},
    {"name": "Zak", "phone": "0631234567", "email": "zak@example.com", "address": "9 Street"}
]

def printAllList():
    for elem in list:
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
    for item in list:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    list.insert(insertPosition, newItem)
    print("New element has been added")
    return

def deleteElementByName(name):
    deletePosition = -1
    for item in list:
        if name == item["name"]:
            deletePosition = list.index(item)
            break
    if deletePosition != -1:
        del list[deletePosition]

def updateElement():
    name = input("Please enter the name of the student to be updated: ")

    student = next((item for item in list if item["name"] == name), None)
    
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
    while True:
        choice = input("Please specify the action [ C create, U update, D delete, P print,  X exit ] ")
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
                print("Exit()")
                break
            case _:
                print("Wrong choice")

main()

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

def addNewElement():
    name = input("Pease enter student name: ")
    phone = input("Please enter student phone: ")
    email = input("Please enter student email: ")
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

def deleteElement():
    name = input("Please enter name to be deleted: ")
    deletePosition = -1
    for item in list:
        if name == item["name"]:
            deletePosition = list.index(item)
            break
    if deletePosition == -1:
        print("Element was not found")
    else:
        del list[deletePosition]
        print(f"Element with name {name} has been deleted.")
    return

def updateElement():
    name = input("Please enter the name of the student to be updated: ")
    updatePosition = -1
    for item in list:
        if name == item["name"]:
            updatePosition = list.index(item)
            break
    if updatePosition == -1:
        print("Element was not found")
        return
    
    print("Leave the field blank if you don't want to update it.")
    phone = input(f"Enter new phone (current: {list[updatePosition]['phone']}): ") or list[updatePosition]['phone']
    email = input(f"Enter new email (current: {list[updatePosition]['email']}): ") or list[updatePosition]['email']
    address = input(f"Enter new address (current: {list[updatePosition]['address']}): ") or list[updatePosition]['address']
    
    updatedItem = {"name": name, "phone": phone, "email": email, "address": address}

    del list[updatePosition]

    insertPosition = 0
    for item in list:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    list.insert(insertPosition, updatedItem)
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
                deleteElement()
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

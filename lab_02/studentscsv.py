import csv

data = [
    {"name": "Bob", "phone": "0631234567", "email": "bob@example.com", "address": "895 Street"},
    {"name": "Emma", "phone": "0631234567", "email": "emma@example.com", "address": "123 Street"},
    {"name": "Jon", "phone": "0631234567", "email": "jon@example.com", "address": "27 Street"},
    {"name": "Zak", "phone": "0631234567", "email": "zak@example.com", "address": "9 Street"}
]

file_name = "students.csv"

# Створення CSV файлу
with open(file_name, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["name", "phone", "email", "address"])
    writer.writeheader()
    writer.writerows(data)

print(f"{file_name} has been created.")

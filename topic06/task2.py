students = [
    {"name": "Катерина", "grade": 100},
    {"name": "Дмитро", "grade": 71},
    {"name": "Максим", "grade": 84},
    {"name": "Аріна", "grade": 95}
]

sortedname = sorted(students, key=lambda student: student["name"])
print("Сортування за ім’ям:")
print(sortedname)

sortedgrade = sorted(students, key=lambda student: student["grade"])
print("\nСортування за оцінкою:")
print(sortedgrade)

sortedgradedesc = sorted(students, key=lambda student: student["grade"], reverse=True)
print("\nСортування за оцінкою у зворотному порядку:")
print(sortedgradedesc)

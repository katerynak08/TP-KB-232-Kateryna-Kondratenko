def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Помилка: ділення на нуль!"

def calculator():
    while True:
        print("Оберіть операцію або введіть 'exit' для виходу:")
        print("1. Додавання")
        print("2. Віднімання")
        print("3. Множення")
        print("4. Ділення")
        
        choice = input("Введіть номер операції (1/2/3/4) або 'exit' для виходу: ").lower()

        if choice == 'exit':
            print("Програма завершена.")
            break
        
        if choice not in ['1', '2', '3', '4']:
            print("Помилка! Спробуйте ще раз.")
            continue

        n1 = float(input("Введіть перше число: "))
        n2 = float(input("Введіть друге число: "))

        if choice == '1':
            print(f"Результат: {n1} + {n2} = {add(n1, n2)}")
        elif choice == '2':
            print(f"Результат: {n1} - {n2} = {subtract(n1, n2)}")
        elif choice == '3':
            print(f"Результат: {n1} * {n2} = {multiply(n1, n2)}")
        elif choice == '4':
            result = divide(n1, n2)
            print(f"Результат: {n1} / {n2} = {result}")

calculator()

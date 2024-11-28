import logging
from functions import add, subtract, multiply, divide
from operations import get_number

logging.basicConfig(
    filename='calc.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class Calculator:
    def __init__(self):
        self.operations = {
            "1": ("Додавання", add),
            "2": ("Віднімання", subtract),
            "3": ("Множення", multiply),
            "4": ("Ділення", divide)
        }

    def log_operation(self, operation_n, n1, n2, result):
        """Логування виконаної операції."""
        logging.info(f"Operation: {operation_n}, Number 1: {n1}, Number 2: {n2}, Result: {result}")

    def run(self):
        while True:
            print("\nОберіть операцію або введіть 'exit' для виходу:")
            print("1. Додавання")
            print("2. Віднімання")
            print("3. Множення")
            print("4. Ділення")
            
            choice = input("Введіть номер операції (1/2/3/4) або 'exit' для виходу: ").lower()

            if choice == 'exit':
                print("Програма завершена.")
                break
            
            if choice not in self.operations:
                print("Помилка! Введіть коректний номер операції.")
                continue

            n1 = get_number("Введіть перше число: ")
            n2 = get_number("Введіть друге число: ")
            
            operation_n, operation_func = self.operations[choice]
            result = operation_func(n1, n2)
            
            print(f"Результат: {operation_n} для {n1} і {n2} = {result}")
            self.log_operation(operation_n, n1, n2, result)

if __name__ == "__main__":
    calc = Calculator()
    calc.run()
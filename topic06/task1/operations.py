def getn(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Помилка: введіть коректне число.")
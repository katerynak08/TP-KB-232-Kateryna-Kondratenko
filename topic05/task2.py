import requests

currency = input("Введіть тип валюти (EUR, USD, PLN): ").upper()
try:
    value = float(input(f"Введіть кількість {currency}: "))
except ValueError:
    print("Помилка: введено некоректне число.")
    exit()

r = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json")

if r.status_code != 200:
    print("Помилка при отриманні даних від API.")
    exit()

currency_rate = None

for elem in r.json():
    if elem['cc'] == currency:
        currency_rate = elem['rate']
        break

if currency_rate is None:
    print(f"Помилка: валюта {currency} не підтримується.")
else:
    result = currency_rate * value
    print(f"Курс {currency} до UAH: {currency_rate}")
    print(f"Результат {value} {currency} у UAH = {result:.2f}")

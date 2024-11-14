import random

choices = ["stone", "scissor", "paper"]

while True:
    user_choice = input("Введіть ваш вибір (stone, scissor, paper) або 'exit' для виходу: ").lower()

    if user_choice == "exit":
        print("Гра завершена!")
        break

    if user_choice not in choices:
        print("Некоректний вибір, спробуйте ще раз.")
        continue

    computer_choice = random.choice(choices)
    print(f"Вибір комп'ютера: {computer_choice}")

    user_index = choices.index(user_choice)
    computer_index = choices.index(computer_choice)

    if user_index == computer_index:
        print("Нічия!")
    elif (user_index - computer_index) % 3 == 1:
        print("Ви виграли!")
    else:
        print("Ви програли!")


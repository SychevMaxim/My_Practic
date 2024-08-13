print('\nЗадача task.7-Пирамидка 2. .\n')

# РЕШЕНИЕ
# Напишите программу, которая получает на вход количество уровней пирамиды и выводит их на экран,
# заполняя нечётными числами:
# =============================



# region {===== Основной код =====}

height = int(input("Введите высоту пирамиды: "))
number = 1

for row in range(height):

    spaces = " " * (height - row - 1)
    print(spaces, end="")

    for col in range(row + 1):

        print(number, end=" ")
        number += 2

    print()

# endregion {===== Основной код =====}
print('\nЗадача task.5-Небольшая. .\n')

# РЕШЕНИЕ
# Пользователь вводит N чисел. Среди натуральных чисел, которые он указал,
# найдите наибольшее по сумме цифр. Выведите на экран это число и сумму его цифр.
# =============================



# region {===== Основной код =====}

n = int(input("Введите количество чисел: "))
max_sum = 0
max_number = 0

for num in range(n):

    number = int(input("Введите число: "))
    current_sum = 0
    temp_number = number

    while temp_number > 0:

        current_sum += temp_number % 10
        temp_number //= 10

    if current_sum > max_sum:

        max_sum = current_sum
        max_number = number

print("Наибольшая сумма цифр у числа", max_number, max_sum)

# endregion {===== Основной код =====}
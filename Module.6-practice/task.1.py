print('\nЗадача task.1. .\n')

# РЕШЕНИЕ
# В один из вечеров
# к Васе домой пришёл племянник и пожаловался на сложности с уроками математики:
# у него никак не получалось разобраться со степенями чисел.
# Вася решил помочь племяннику и написать программу,
# которая позволит наглядно увидеть возведение чисел в третью степень.
#
# Напишите программу, которая возводит в третью степень каждое число от 1 до N и выводит результат на экран.
# =============================



# region {===== Основной код =====}

number = int(input("Введите число"))
count = 0

while count != number:

	count += 1
	multiplication = count ** number
	print(multiplication)


# endregion {===== Основной код =====}
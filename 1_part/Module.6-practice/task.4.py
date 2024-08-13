print('\nЗадача task.4. .\n')

# РЕШЕНИЕ
# Напишите программу, которая находит количество положительных и количество отрицательных чисел в последовательности.
# Последовательность заканчивается на числе 0.
# =============================


# region {===== Основной код =====}
#region {===== Первый способ =====}
# first_number = int(input('Введите оценку: '))
# second_number = int(input('Введите оценку: '))
# third_number = int(input('Введите оценку: '))
# fourth_number = int(input('Введите оценку: '))
# count_number = 4
number_positive = 0
number_negative = 0
# count_repeat = number_negative + number_positive
# summ = 0
#
# if first_number > 0:
# 	number_positive += 1
# elif first_number < 0:
# 	number_negative += 1
#
# if second_number > 0:
# 	number_positive += 1
# elif second_number < 0:
# 	number_negative += 1
#
# if third_number > 0:
# 	number_positive += 1
# elif third_number < 0:
# 	number_negative += 1
#
# if fourth_number > 0:
# 	number_positive += 1
# elif fourth_number < 0:
# 	number_negative += 1
# endregion {===== Первый способ =====}
#region {===== Второй способ =====}
count_number = 4

while count_number != 0:

	count_number -= 1
	number = int(input("Введите число: "))
	if number > 0:
		number_positive += 1

	elif number < 0:
		number_negative += 1
	else:
		break

print("число позитивных  оценок: ", number_positive)
print("число негативных оценок: ", number_negative)
# endregion {===== Второй способ =====}
# endregion {===== Основной код =====}
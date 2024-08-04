print('\nЗадача task.8-яма. .\n')

# РЕШЕНИЕ
# Представьте, что вы разрабатываете компьютерную игру с текстовой графикой. Вам поручили создать генератор
# ландшафта. Напишите программу, которая получает на вход число N и выводит на экран числа в виде ямы:
# =============================



# region {===== Основной код =====}

# number = int(input())
# start = 1
# stop = number * 2
# last_num = ""
# num = number * 2 - 2
# for col in range (number * 2):
# 	for row in range(1, number + 1):
# 		if row == start or row == stop:
# 			last_num += str(number)
# 			print(last_num + "." * num, end="")
# 			print(last_num[::-1])
# 			start += 1
# 			stop -= 1
# 		num -= 2
# 		number -= 1
depth = int(input("введите глубину ямы: "))

for line in range(depth):
	for left_number in range(depth, depth - line - 1, -1):
		print(left_number, end="")

	print("." * (2 * (depth - line - 1)), end="")

	for right_number in range(depth - line, depth + 1):
		print(right_number, end="")

	print()

# endregion {===== Основной код =====}
print('\nЗадача task.2-Лестница. .\n')

# РЕШЕНИЕ
# Напишите программу,
# которая выводит «лестницу» из чисел, когда пользователь вводит число N:
# =============================





# region {===== Основной код =====}

start = 1
x = 0
stop = int(input("Введите число"))

while x != stop:

	for number in range(start, stop + 1):
		x += 1
		print(str(number) * x)

	start += 1

	print()

# endregion {===== Основной код =====}
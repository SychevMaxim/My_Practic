print('\nЗадача task.6-Пирамидка. .\n')

# РЕШЕНИЕ
# Напишите программу, которая выводит на экран равнобедренный треугольник (пирамидку),
# заполненный символами хештега (#). Пусть высоту пирамиды определяет пользователь.


# =============================





# region {===== Основной код =====}

height = int(input("Введите высоту пирамидки"))
count_heshteg = 0
count = height

while count_heshteg != height:
	for col in range (height + 1):

		if col >= height and col <= height + count_heshteg:

			print(" " * count + "# " + count_heshteg * "# ")

			count -= 1
			count_heshteg += 1

# endregion {===== Основной код =====}
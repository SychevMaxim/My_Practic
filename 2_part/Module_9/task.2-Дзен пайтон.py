print('\nЗадача . .\n')

# РЕШЕНИЕ
# Напишите программу, которая выводит на экран все строки этого файла в обратном порядке.
# =============================





# region {===== Основной код =====}

speaker_file = open('zen.txt')
lst = []
for letter in speaker_file:
	lst.append(letter)
for letter in reversed(lst):
	print(letter)

# endregion {===== Основной код =====}
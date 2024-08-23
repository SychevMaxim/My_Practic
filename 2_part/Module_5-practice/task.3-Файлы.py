print('\nЗадача 3.Файлы.\n')

# РЕШЕНИЕ
# Напишите программу, которая получает на вход полное название файла и проверяет, соответствует ли он этим правилам.
# =============================





# region {===== Основной код =====}

danger_symbal = '@, №, $, %, ^, &, *, ()'.split(',')
string = input('Название файла: ')

TorF = True

for letter in danger_symbal:

	if string.startswith(letter):
		TorF = False

if TorF == False:
	print('Ошибка: название начинается недопустимым символом.')

else:

	if string.endswith('.txt') or string.endswith('.docx'):
		print('Файл назван корректно')

	else:
		print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx.')

# endregion {===== Основной код =====}
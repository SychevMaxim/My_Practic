print('\nЗадача task.5. .\n')

# РЕШЕНИЕ
#Вася вдохновился фильмом «Двадцать одно» и решил изучить математику игровых автоматов. Для анализа данных ему нужна информация о том, как часто в автомате выпадает три или две одинаковых картинки. Для сбора данных нужна программа, проверяющая это равенство.

#Даны три целых числа. Определите, сколько среди них совпадающих. Программа должна вывести одно из чисел: 3 (если все
# совпадают), 2 (если два совпадают) или 0 (если все числа разные).
# =============================





# region {===== Основной код =====}

first_number = int(input('Введите первое число'))
second_number = int(input('Введите второе число'))
third_number = int(input('Введите третье число'))
if first_number == second_number == third_number:
	print('3')
if (first_number == second_number != third_number or second_number == third_number != first_number or third_number ==
	first_number != second_number):
	print("2")
if first_number != second_number != third_number:
	print("0")

# endregion {===== Основной код =====}
print('\nЗадача . .\n')

# РЕШЕНИЕ
# Как вы знаете, в Python есть полезная функция sum, которая умеет находить сумму элементов списков. Иногда базовых возможностей функций не хватает для работы и приходится их усовершенствовать.
#
# Напишите свою функцию sum, которая должна быть более гибкой, чем стандартная. Она должна уметь складывать числа:
#
# из списка списков,
# набора параметров.
# Основной код оставьте пустым или закомментированным (используйте его только для тестирования).
#
# Примеры вызовов функции
#
# sum([[1, 2, [3]], [1], 3])
#
# Ответ в консоли: 10
#
# sum(1, 2, 3, 4, 5)
#
# Ответ в консоли: 15
# =============================





# region {===== Основной код =====}

# функция для извлечения чисел из списков
def sub_summ(name, summ = 0, full_name = []):
	if isinstance(name, list):
		for letter in name:
			if letter != []:
				if isinstance(letter, list):
					return sub_summ(letter, summ, name)
				else:
					summ += letter
					name.remove(letter)
					return sub_summ(full_name, summ, full_name)
			else:
				name.remove(letter)
				return sub_summ(name, summ, name)
	else:
		summ += int(name)
	return summ
# функция проверяющая является ли элемент списком, если да то перекидывает его на другую функцию
def summ(name, summ):
	if isinstance(name, list):
		for letter in name:
			summ += sub_summ(name)
	return summ
print(summ([[1, 2, [3]], [1], 3, [2]], 0))

# endregion {===== Основной код =====}
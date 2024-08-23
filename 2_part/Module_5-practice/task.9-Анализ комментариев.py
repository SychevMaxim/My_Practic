print('\nЗадача 9.Анализы комментариев.\n')

# РЕШЕНИЕ
# Напишите программу, которая считывает строку и выводит количество заглавных и строчных букв в строке,
# используя методы строк.

# Программа должна это делать за один проход по строке.
#
# Решение должно быть оформлено в виде функции, которая принимает на вход строку-текст,
# а на выход возвращает два числа (количество заглавных и строчных букв).
# =============================





# region {===== Основной код =====}

def count_uppercase_lowercase(text, count_upper, count_lower):
	for letter in text:

		if letter.isupper():
			count_upper += 1

		elif letter.islower():
			count_lower += 1

	return count_upper, count_lower


text = input("Введите строку для анализа: ")

uppercase, lowercase = count_uppercase_lowercase(text, 0, 0)

print("Количество заглавных букв:", uppercase)
print("Количество строчных букв:", lowercase)

# endregion {===== Основной код =====}
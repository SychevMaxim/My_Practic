print('\nЗадача 6.Сжатие.\n')

# РЕШЕНИЕ
# Напишите программу, которая считывает строку, кодирует её, используя предложенный алгоритм, и выводит
# закодированную последовательность на экран. Код должен учитывать регистр символов.

# Пример
#
# Введите строку: aaAAbbсaaaA.
#
# Закодированная строка: a2A2b2с1a3A1.
# =============================





# region {===== Основной код =====}

string = list(input('Введите строку: '))
counter = 0
lst_letter = []

for count in range(len(string)):

	if count != len(string) - 1 and string[count] == string[count + 1]:
		counter += 1

	else:

		print(f'{string[count]}{counter + 1}', end='')
		counter = 0

# endregion {===== Основной код =====}
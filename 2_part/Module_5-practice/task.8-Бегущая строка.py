print('\nЗадача 8.Бегущая строка.\n')

# РЕШЕНИЕ
# Пользователь вводит две строки. Напишите программу, которая определяет, можно ли получить первую строку из второй
# циклическим сдвигом.

# По желанию: если строку получить можно, выведите значение сдвига.
#
# Пример 1
#
# Первая строка: abcd.
#
# Вторая строка: cdab.
#
# Первая строка получается из второй со сдвигом 2.
# =============================





# region {===== Основной код =====}

first_string = input('Введите строку: ')
second_string = input('введите строку: ')

count_try = 0

full_string = first_string + first_string

start_point = len(first_string)
stop_point = len(full_string)

for num in range(len(first_string)):

	if full_string[start_point:stop_point] == second_string:

		print(f'Первая строка получается из второй с сдвигом {count_try}')
		break

	else:

		start_point -= 1
		stop_point -= 1
		count_try += 1

# endregion {===== Основной код =====}
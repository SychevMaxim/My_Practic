print('\nЗадача 7.ip адрес.\n')

# РЕШЕНИЕ
# Пользователь вводит строку. Напишите программу, которая определяет, действительно ли заданная строка — правильный
# IP-адрес. Обеспечьте контроль ввода, где предусматривается добавление целых чисел от 0 до 255 и точек между ними.

# Пример 1
#
# Введите IP: 128.16.35.a4
#
# a4 — это не целое число.
#
# Пример 2
#
# Введите IP: 240.127.56.340
#
# 340 превышает 255.
#
# Пример 3
#
# Введите IP: 34.56.42,5
#
# Адрес — это четыре числа, разделённые точками.
#
# Пример 4
#
# Введите IP: 128.0.0.255
#
# IP-адрес корректен.
# =============================





# region {===== Основной код =====}

number_lst = list('1234567890.,!=-')
str_ip = ''
count_point = 0


def IP(count_point):
	ip = input('IP: ')

	for symbal in ip:

		if symbal not in number_lst:
			print(f'"{symbal}" не является числом')
			continue

	for point in ip:

		if point == '.':
			count_point += 1

	if count_point != 3:
		print('Адрес — это четыре числа, разделённые точками.')

	ip = ip.split('.')

	for num in ip:

		if int(num) > 255:
			print(f'{num} превышает 255')

	else:
		print(f'IP адрес корректен')


IP(count_point)

# endregion {===== Основной код =====}
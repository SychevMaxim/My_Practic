print('\nЗадача 2. Универсальная программа.\n')

# РЕШЕНИЕ
# Напишите функцию, возвращающую список элементов итерируемого объекта (кортежа, строки, списка, словаря),
# у которых индекс — это простое число.

# Для проверки на простое число напишите отдельную функцию is_prime.
#
# Необязательное усложнение: сделайте так, чтобы основная функция состояла только из оператора return
# и так же возвращала список.
#
# Пример вызова функции:
#
# print(crypto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
#
# Ответ в консоли: [2, 3, 5, 7]
#
# Пример вызова функции:
#
# print(crypto('О Дивный Новый мир!'))
#
# Ответ в консоли: ['Д', 'и', 'н', 'й', 'в', 'й', 'р']
#
# Советы и рекомендации
# Для нумерации элементов используйте функцию enumerate. Это позволит работать одинаково со всеми структурами данных.
# =============================





# region {===== Основной код =====}

def is_prime(string):

	prime_lst = []
	prime_flag = False

	def for_list(string, prime_flag):
		for i_key in range(2, len(string)):
			for prime in range(2, i_key):
				if i_key % prime == 0:
					prime_flag = True
			if prime_flag is False:
				prime_lst.append(string[i_key])
			prime_flag = False
	if type(string) == list:
		for_list(string, prime_flag)
	else:
		string = list(string)
		for_list(string, prime_flag)
	return prime_lst
string = 'О Дивный Новый мир!'
is_prime(string)
def crypto():
	return is_prime(string)

crypto()


print(crypto())

# endregion {===== Основной код =====}
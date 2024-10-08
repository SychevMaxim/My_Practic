print('\nЗадача 6. контакты.\n')

# РЕШЕНИЕ
# Напишите программу, которая бесконечно запрашивает у пользователя действие, которое он хочет совершить: добавить
# контакт или найти человека в списке контактов по фамилии.

# Действие «добавить контакт»: программа запрашивает имя и фамилию контакта, затем номер телефона,
# добавляет их в словарь и выводит на экран текущий словарь контактов. Если этот человек уже есть в словаре,
# то выводится соответствующее сообщение.
#
# Действие «поиск человека по фамилии»:
# программа запрашивает фамилию и выводит все контакты с такой фамилией и их номера телефонов.
# Поиск не должен зависеть от регистра символов.
#
# Пример работы программы:
#
# Введите номер действия:
#
# Добавить контакт.
# Найти человека.
# При выборе действия 1:
#
# Введите имя и фамилию нового контакта (через пробел): Иван Сидоров
#
# Введите номер телефона: 888
#
# Текущий словарь контактов: {('Иван', 'Сидоров'): 888}
#
# Введите номер действия:
#
# Добавить контакт
# Найти человека
# При выборе действия 1:
#
# Введите имя и фамилию нового контакта (через пробел): Иван Сидоров
#
# Такой человек уже есть в контактах.
#
# Текущий словарь контактов: {('Иван', 'Сидоров'): 888}
#
# Введите номер действия:
#
# Добавить контакт
# Найти человека
# При выборе действия 1:
#
# Введите имя и фамилию нового контакта (через пробел): Алиса Петрова
#
# Введите номер телефона: 999
#
# Текущий словарь контактов: {('Иван', 'Сидоров'): 888, ('Алиса', 'Петрова'): 999}
#
# Введите номер действия:
#
# Добавить контакт
# Найти человека
# При выборе действия 2:
#
# Введите фамилию для поиска: Сидоров
#
# Иван Сидоров 888
#
# Введите номер действия:
#
# Добавить контакт
# Найти человека

# =============================





# region {===== Основной код =====}

phone_dict = {}
while True:
	print(phone_dict)
	activity = int(input(f'Введите номер действия 1 - Добавить человека 2 - найти человека: '))
	if activity == 1:
		name = tuple(input('Введите имя и фамилию нового контакта (через пробел):').split())
		print(name)
		if not name in phone_dict:
			phone = int(input('Введите номер телефона'))
			phone_dict[name] = phone
		else:
			print('Этот человек уже есть в книжке')
	else:
		name = input('введите имя человека которого хотите найти: ')
		if tuple(name.split()) in phone_dict.keys():
			print(name, phone_dict[tuple(name.split())])
			print(1)

# endregion {===== Основной код =====}
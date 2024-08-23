print('\nЗадача Вечеринка. .\n')

# РЕШЕНИЕ
# Напишите программу, которая спрашивает у пользователя, ушёл ли человек и пришёл ли новый гость, и,
# исходя из ответа, добавляет в список или удаляет из него нужное имя. При этом гостей может быть не больше шести.
# Имена запрашиваются до тех пор, пока пользователь не введёт сообщение «Пора спать»
# =============================





# region {===== Основной код =====}

def activitty(activity, count_guests):

	while True:

		print('Текущий список:', guests)
		activity = input('Гость пришел или ушел?')

		if activity == 'Пора спать':

			print('Вечеринка окончена, все пошли спать!')
			break

		else:
			name = input("Введите имя: ")
			if activity == 'пришел':

				guests.append(name)
				count_guests += 1

			elif activity == 'ушел':

				guests.remove(name)
				count_guests -= 1

		if count_guests >= 7:

			print('мест больше нет')
			count_guests -= 1
			guests.remove(name)

guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
count_guests = len(guests)
activity = ''
if count_guests < 7:
	activitty(activity, count_guests)
elif count_guests >= 7:
	print('Мест больше нет')


# endregion {===== Основной код =====}
print('\nЗадача 5.Пароль.\n')

# РЕШЕНИЕ
#Напишите программу, которая просит пользователя придумать пароль до тех пор, пока этот пароль не станет надёжным. Должна использоваться латиница.

# Пример
#
# Придумайте пароль: qwerty.
#
# Пароль ненадёжный. Попробуйте ещё раз.
#
# Придумайте пароль: qwerty12.
#
# Пароль ненадёжный. Попробуйте ещё раз.
#
# Придумайте пароль: qwerty123.
#
# Пароль ненадёжный. Попробуйте ещё раз.
#
# Придумайте пароль: qWErty123.
#
# Это надёжный пароль.
# =============================





# region {===== Основной код =====}

TorF = False

while True:
	string = input('Введите строку: ')
	for letter in string:
		if letter.isupper():
			TorF = True
	if TorF == True:
		print('Это надежный пароль.')
		break
	else:
		print('Пароль ненадёжный. Попробуйте ещё раз.')

# endregion {===== Основной код =====}
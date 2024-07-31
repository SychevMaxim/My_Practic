
# region {===== Код Макса =====}

# ширина поля по Х
# max_x = 15
# # длина поля
# max_y = 20
# # текущее положение по x
# current_x = 8
# # Текущее положение по y
# curent_y = 10
# # нажатая клавиша
# input_key = ""
#
# # вывод команд управления марсоходом
# print() # пустая строка
# print('=' * 20) # выделяю команды управления
# print('[Программа]: Команды управления марсоходом: ')
# print('север (клавиша W), юг (клавиша S), запад (клавиша A)', 'восток (клавиша D). Выход (клавиша Q)')
# print('=' * 20) # выделяю команды управления
#
# while input_key != 'q':
#
# 	print("текущие координаты равны:", current_x, curent_y)
# 	print("в какую сторону вы хотите направить робота: ")
# 	input_key = input("север (клавиша W), юг (клавиша S), запад (клавиша A) или восток (клавиша D) ")
#
# 	if current_x == 0:
#
# 		if input_key == "w":
#
# 			current_x += 1
# 			print(input_key)
#
# 		elif input_key == "d":
# 			curent_y += 1
#
# 		elif input_key == "a":
# 			curent_y -= 1
# 		continue
#
# 	elif curent_y == 0:
#
# 		if input_key == "d":
# 			curent_y += 1
#
# 		elif input_key == "w":
# 			current_x += 1
# 		elif input_key == "s":
# 			current_x -= 1
#
# 	elif current_x == 15 or curent_y == 20:
#
# 		if input_key == "s":
# 			current_x -= 1
#
# 		elif input_key == "a":
# 			curent_y -= 1
#
# 		continue
#
# 	if input_key == "w":
#
# 		current_x += 1
# 		print(input_key)
#
# 	elif input_key == "s":
# 		current_x -= 1
#
# 	elif input_key == "d":
# 		curent_y += 1
#
# 	elif input_key == "a":
# 		curent_y -= 1


# endregion {===== Код Макса =====}


# region {===== Мой код =====}

# ширина поля по Х
max_x = 15
# длина поля
max_y = 20
# текущее положение по x
current_x = 8
# Текущее положение по y
current_y = 10
# нажатая клавиша
input_key = ""

# вывод команд управления марсоходом
print() # пустая строка
print('=' * 20) # выделяю команды управления
print('[Программа]: Команды управления марсоходом: ')
print('север (клавиша W), юг (клавиша S), запад (клавиша A)', 'восток (клавиша D). Выход (клавиша Q)')
print('=' * 20) # выделяю команды управления

while input_key != 'q':

	# получение команды
	print('[Программа]: Марсоход находится на позиции', current_x, current_y), 'введите команду:'
	input_key = input('[Оператор]: ')

	# определяем нажатую клавишу

	# нажата 'W'
	if (input_key == 'W') and (current_y < max_y):
		current_y += 1
	elif (input_key == 'W'):
		print('[Программа]: Марсоход уперся в стену!')

	# нажата 'S'
	elif (input_key == 'S') and (current_y > 0):
		current_y -= 1
	elif (input_key == 'S'):
		print('[Программа]: Марсоход уперся в стену!')

	# нажата 'A'
	elif (input_key == 'A') and (current_x > 0):
		current_x -= 1
	elif (input_key == 'A'):
		print('[Программа]: Марсоход уперся в стену!')

	# нажата 'D'
	elif (input_key == 'D') and (current_x < max_x):
		current_x += 1
	elif (input_key == 'D'):
		print('[Программа]: Марсоход уперся в стену!')

	# нажата 'Q'
	elif (input_key == 'Q'):
		print()  # пустая строка
		print('=' * 20)  # выделяю команды управления
		print('[Программа]: Завершение управления.')
		print('[Программа]: Выход из программы.')
		print('=' * 20)  # выделяю команды управления
		break

	# нажата другая клавиша, кроме 'Q'
	else:
		print()  # пустая строка
		print('=' * 20)  # выделяю команды управления
		print('[Программа]: Команда не верна!')
		print('[Программа]: Команды управления марсоходом: ')
		print('север (клавиша W), юг (клавиша S), запад (клавиша A)',
			  'восток (клавиша D). Выход (клавиша Q)')
		print('=' * 20)  # выделяю команды управления

# endregion {===== Мой код =====}
print('\nЗадача . .\n')

# РЕШЕНИЕ
# У вас есть файл с протоколом регистрации пользователей на сайте — registrations.txt. Каждая строка содержит имя, имейл и возраст, разделённые пробелами. Например: Василий test@test.ru 27.
#
# Напишите программу, которая проверяет данные из файла для каждой строки:
#
# Присутствуют все три поля.
# Поле «Имя» содержит только буквы.
# Поле «Имейл» содержит @ и точку.
# Поле «Возраст» представляет число от 10 до 99.
# В результате проверки сформируйте два файла:
#
# registrations_good.log для правильных данных; записывать строки как есть;
# registrations_bad.log — для ошибочных; записывать строку и вид ошибки.
# Для валидации строки данных напишите функцию, которая может выдавать исключения:
#
# НЕ присутствуют все три поля: IndexError.
# Поле «Имя» содержит НЕ только буквы: NameError.
# Поле «Имейл» НЕ содержит @ и точку: SyntaxError.
# Поле «Возраст» НЕ представляет число от 10 до 99: ValueError.
# Формат выходных данных
#
# Содержимое файла registrations_bad.log:
#
# Ольга kmrn@gmail.com 123        Поле «Возраст» НЕ представляет число от 10 до 99
#
# Чехова kb@gmail.com 142        Поле «Возраст» НЕ представляет число от 10 до 99
#
# ……
#
# Степан ky 59        Поле «Имейл» НЕ содержит @ и точку
#
# ……
#
# Содержимое файла registrations_good.log:
#
# Геннадий ttdababmt@gmail.com 69
#
# Ольга ysbxur@gmail.com 20
#
# ……
# =============================





# region {===== Основной код =====}


list_data = ()
index_error = ()
name_error = ()
syntax_error = ()
value_error = ()
good = ()

for letter in open('registrations.txt', encoding='UTF-8'):

	sub_letter = letter.split()
	if len(sub_letter) != 3:
		index_error += (letter, 'НЕ присутствуют все три поля: IndexError')

	elif not isinstance(sub_letter[0], str):
		name_error += (letter, 'Поле «Имя» содержит НЕ только буквы: NameError.')

	elif '@' not in sub_letter[1].split() and '.' not in sub_letter[1].split():
		syntax_error += (letter, 'Поле «Имейл» НЕ содержит @ и точку: SyntaxError')

	elif sub_letter[2] not in range(10, 99):
		value_error += (letter, 'Поле «Возраст» НЕ представляет число от 10 до 99')
	else:
		good += letter

for letter in index_error:
	open('registrations_bad.log', 'a', encoding='UTf-8').write(letter)



for letter in name_error:
	open('registrations_bad.log', 'r', encoding='UTf-8').write(letter)

for letter in syntax_error:
	open('registrations_bad.log', 'a', encoding='UTf-8').write(letter)

for letter in value_error:
	open('registrations_bad.log', 'a', encoding='UTf-8').write(letter)
	print('.'*6)
for letter in open('registrations_bad.log', 'r'):
	print(letter)

# endregion {===== Основной код =====}
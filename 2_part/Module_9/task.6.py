print('\nЗадача . .\n')

# РЕШЕНИЕ
# Мало кто не знает знаменитый роман Л. Н. Толстого «Война и мир». Это довольно объёмное произведение лежит в архиве voina-i-mir.zip. Напишите программу, которая подсчитывает статистику по буквам (не только русского алфавита) в этом романе и выводит результат на экран (или в файл). Результат должен быть отсортирован по частоте встречаемости букв (по возрастанию или убыванию). Регистр символов имеет значение.
#
# Архив можно распаковать вручную, но, если хотите, можете изучить документацию по модулю zipfile (можно использовать и другой модуль) и попробовать написать код, который будет распаковывать архив за вас.
# =============================





# region {===== Основной код =====}

import zipfile

symbol_dict = {}

extract_dir = ''
zip_arh = 'war_and_peace.ru.zip'

zip_dir = ''

result_file = 'result.txt'
with zipfile.ZipFile(zip_arh, 'r') as zip_file:
	zip_file.extractall(extract_dir)

zip_file.close()

read_file = open('war_and_peace.ru.txt',  'r', encoding='utf-8')
read_file = read_file.read()

for letter in read_file:
	symbol_dict[letter] += 1

for key, value in sorted(symbol_dict.items(), key = lambda x: int(x[1]), reverse = True):
	print(key, ':', value)

# endregion {===== Основной код =====}
print('\nЗадача 3. Файлы и папки.\n')

# РЕШЕНИЕ
# Напишите программу, которая получает на вход путь до каталога (в том числе это может быть просто корень диска) и выводит общее количество файлов и подкаталогов в нём. Также выведите на экран размер каталога в килобайтах (1 килобайт = 1024 байт).
#
# Важный момент: чтобы посчитать, сколько весит каталог, нужно найти сумму размеров всех вложенных в него файлов.
#
# Результат работы программы на примере python_basic\Module14:
#
# E:\PycharmProjects\python_basic\Module14
#
# Размер каталога (в Кбайтах): 8.373046875
#
# Количество подкаталогов: 7
#
# Количество файлов: 15
# =============================


import os

counters = {
	# кол-во подкаталогов
	'folder_count' : 0,
	# кол-во файлов
	'files_count' : 0,
	# размер подкаталога
	'folder_size' : 0
}


def geting_size(currrent_path, counters):
	for i_elem in os.listdir(currrent_path):
		path = os.path.join(currrent_path, i_elem)
		if os.path.isfile(path):
			counters['files_count'] += 1
			counters['folder_size'] += os.path.getsize(path)
		elif os.path.isdir(path):
			counters['folder_count'] += 1
			geting_size(path, counters)
	return

folder_path = os.path.abspath('..')
print(folder_path)

# проходимся по папкам
geting_size(folder_path, counters)

print(f'Размер каталога (в Кбайтах): {round(counters['folder_size'] / 1024, 2)}')
print(f'Количество подкаталогов: {counters['folder_count']}')
print(f'Количество файлов: {counters['files_count']}')
print('\nЗадача . .\n')

# РЕШЕНИЕ
# В файле first_tour.txt записано число K и данные об участниках турнира по настольной игре «Орлеан»: фамилии, имена и количество баллов, набранных в первом туре. Во второй тур проходят участники, которые набрали более K баллов в первом туре.
#
# Напишите программу, которая выводит в файл second_tour.txt данные всех участников, прошедших во второй тур, с нумерацией.
#
# В первой строке нужно вывести в файл second_tour.txt количество участников второго тура. Затем программа должна вывести фамилии, инициалы и количество баллов всех участников, прошедших во второй тур, с нумерацией. Имя нужно сократить до одной буквы. Список должен быть отсортирован по убыванию набранных баллов.
#
# Пример:
#
# Содержимое файла first_tour.txt:
#
# 80
#
# Ivanov Serg 80
#
# Sergeev Petr 92
#
# Petrov Vasiliy 98
#
# Vasiliev Maxim 78
#
# Содержимое файла second_tour.txt:
#
# 2
#
# 1) V. Petrov 98
#
# 2) P. Sergeev 92
# =============================





# region {===== Основной код =====}

import os

lst = []
first = {
	'name': '',
	'score': 0
}
second = {
	'name': '',
	'score': 0
}
for letter in open('first_tour.txt'):
	print(letter)
	lst.append(letter.split())
for lettter in lst:
	if int(lettter[2]) > first['score']:
		second['score'] = first['score']
		second['name'] = first['name']
		first['score'] = int(lettter[2])
		first['name'] = lettter[:2]
print()
print('Содержимое файла second_tour.txt: ')
print('')
print(first['name'], first['score'])
print(second['name'], second['score'])


# endregion {===== Основной код =====}
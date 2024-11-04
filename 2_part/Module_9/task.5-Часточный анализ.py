print('\nЗадача . .\n')

# РЕШЕНИЕ
# Есть файл text.txt, который содержит текст. Напишите программу, которая выполняет частотный анализ, определяя долю каждой буквы английского алфавита в общем количестве английских букв в тексте, и выводит результат в файл analysis.txt. Символы, не являющиеся буквами английского алфавита, учитывать не нужно.
#
# В файл analysis.txt выводится доля каждой буквы, встречающейся в тексте, с тремя знаками в дробной части. Буквы должны быть отсортированы по убыванию их доли. Буквы с равной долей должны следовать в алфавитном порядке.
#
# Пример:
#
# Содержимое файла text.txt:
#
# Mama myla ramu.
#
# Содержимое файла analysis.txt:
#
# a 0.333
#
# m 0.333
#
# l 0.083
#
# r 0.083
#
# u 0.083
#
# y 0.083
# =============================





# region {===== Основной код =====}

lst = {}
for letter in open('text.txt'):
	for sub_list in letter.lower():
		if sub_list != ' ' and sub_list != '.':
			if sub_list in lst:
				lst[sub_list] += 1
			else:
				lst[sub_list] = 1
last_num = 0
lst_value = []
for letter, value in lst.items():
	lst[letter[0]] /= 26
	lst_value.append(value)
lst = sorted(lst.items(), key=lambda x: x[1], reverse=True)
for letter in lst:
	print(letter[0], '=', round(letter[1], 3))


# endregion {===== Основной код =====}
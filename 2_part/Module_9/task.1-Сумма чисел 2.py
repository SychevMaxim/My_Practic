print('\nЗадача . .\n')

# РЕШЕНИЕ
# Во входном файле numbers.txt записано N целых чисел, которые могут быть разделены пробелами и концами строк. Напишите программу, которая выводит сумму чисел во выходной файл answer.txt.
#
# Пример:
#
# Содержимое файла numbers.txt
#      2
# 2
#   2
#         2
#
# Содержимое файла answer.txt
#
# 8
# =============================





# region {===== Основной код =====}

import os
speakers_file = open('numbers.txt')
print('Содержание файла numbers.txt:')
summ_file = open('answer.txt', 'w')
summ = 0
for letter in speakers_file:
	print(letter)
	summ += int(letter)
speakers_file.close()
open('answer.txt')
summ_file.write(str(summ))
summ_file.close()
print('значенниe answer.txt:')
print(summ)

# endregion {===== Основной код =====}
print('\nЗадача 4. По парам.\n')

# РЕШЕНИЕ
# Напишите программу, которая инициализирует список из 10 случайных целых чисел, а затем делит эти числа на пары
# кортежей внутри списка. Выведите результат на экран.

# Дополнительно: решите задачу несколькими способами.
#
# Пример:
#
# Оригинальный список: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# Новый список: [(0, 1), (2, 3), (4, 5), (6, 7), (8, 9)]
# =============================





# region {===== Основной код =====}

import random
original_list = [int(random.random() * 10) for _ in range(10)]
final_list = []
print(original_list)
for counter in range(0, len(original_list), 2):
	final_list.append((original_list[counter], original_list[counter + 1]))
print(final_list)

# endregion {===== Основной код =====}
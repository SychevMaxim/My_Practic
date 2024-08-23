print('\nЗадача 3.Случайное соревнование.\n')

# РЕШЕНИЕ
# Напишите программу, которая генерирует два списка участников (по 20 элементов) из случайных вещественных чисел (от
# 5 до 10). Для этого найдите подходящую функцию из модуля random.
# Затем сгенерируйте третий список, в котором окажутся только победители из каждой пары.
# =============================





# region {===== Основной код =====}

import random

first_group = [round(random.randint(5, 10) + random.random(), 2) for _ in range(20)]
second_group = [round(random.randint(5, 10) + random.random(), 2) for _ in range(20)]
winer = [first_group[counter] if first_group[counter] >= second_group[counter] else second_group[counter] for counter in range(0, 20)]

print('Первая команда', first_group)
print('Вторая команда', second_group)
print('Победители:', winer)

# endregion {===== Основной код =====}
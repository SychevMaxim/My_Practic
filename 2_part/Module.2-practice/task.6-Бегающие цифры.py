print('\nЗадача Бегущая строка. .\n')

# РЕШЕНИЕ
# Вы пишете программу для маленького табло, в котором циклически повторяется один и тот же текст или числа,
# например как в метро, автобусах или трамваях.

# Дан список из N элементов и целое число K. Напишите программу, которая циклически сдвигает элементы списка вправо на
# K позиций. Используйте минимально возможное количество операций присваивания.
# =============================


# region {===== Основной код =====}

# shift = int(input("Введите сдвиг: "))
# current_list = list(input("Введите  список: "))
#
# new_list = []
#
# for num in range(len(current_list)):
#
# 	if num >= shift - 1:
# 		new_list.append(current_list[num])
# for number in range(shift):
#
# 	if number < shift - 1:
# 		new_list.append(current_list[number])
#
# print('Старый список:', current_list)
# print('новый список:', new_list)

# endregion {===== Основной код =====}

# region {===== NewCode =====}

shift = int(input("Введите сдвиг: ")) # сдвиг 3
current_list = [1, 2, 3, 4, 5]
last_num = len(current_list) - shift


new_list = []
for right_number in range(last_num, len(current_list)):
	new_list.append(current_list[right_number])
for left_num in range(0, last_num):
	new_list.append(current_list[left_num])
print(new_list)


# endregion {===== NewCode =====}
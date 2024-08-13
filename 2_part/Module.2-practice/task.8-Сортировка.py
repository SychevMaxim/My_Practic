print('\nЗадача Сортировка. .\n')

# РЕШЕНИЕ
# Дан список из N чисел. Напишите программу, которая сортирует элементы списка по возрастанию и выводит их на экран.
# Дополнительный список использовать нельзя.

# Также нельзя использовать готовые функции sorted/min/max и метод sort

# Постарайтесь придумать и написать как можно более эффективный алгоритм сортировки.
# =============================



# region {===== Основной код =====}

def sort_list_in_place(current_list):

	for min_i in range(len(current_list)):
		for current_min in range(min_i, len(current_list)):
			if current_list[current_min] < current_list[min_i]:
				current_list[current_min], current_list[min_i] = current_list[min_i], current_list[current_min]


nums = [4, 9, 7, 6, 3, 4]
sort_list_in_place(nums)
print(nums)

# endregion {===== Основной код =====}
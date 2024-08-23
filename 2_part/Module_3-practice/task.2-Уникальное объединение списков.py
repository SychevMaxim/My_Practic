print('\nЗадача .Уникальное объединение списков .\n')

# РЕШЕНИЕ
# Напишите программу, которая объединяет два отсортированных списка целых чисел в один отсортированный список без
# дубликатов.
# =============================





# region {===== Основной код =====}

def merge_sorted_lists(list1, list2):

	gap = len(list2)
	count = 0
	list1.extend(list2)
	list2 = []
	print(list1)

	for min_i in range(len(list1) // 2):

		list2.append(str(list1[count]))
		list2.append(str(list1[gap]))
		count += 1
		gap += 1

	return list2



list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 6, 8, 10]

merged = merge_sorted_lists(list1, list2)
print(merged)

# endregion {===== Основной код =====}
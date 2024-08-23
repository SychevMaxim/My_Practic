print('\nЗадача . Симметричная последовательность.\n')

# РЕШЕНИЕ
# Пользователь вводит последовательность из N чисел. Напишите программу, которая определяет, какое минимальное
# количество и каких чисел нужно добавить в конец этой последовательности, чтобы она стала симметричной.
# =============================





# region {===== Мой код(ошибочный) =====}
#
# num = list(input("Введите список"))
# revers_num = []
# counter = len(num) - 1
#
# min = 0
# for _ in range(len(num)):
#
# 	revers_num.append(num[counter])
# 	counter -= 1
#
# counter = len(num) - 1
#
# if num == revers_num:
# 	print('Число симетрично')
#
# else:
#
# 	if int(num[counter]) == int(num[counter]) - 1:
#
# 		min += 1
# 		counter -= 1
#
# 	for _ in range(min):
#
# 		num.append(num[len(num) - 1])
# 		print(min)
#
# 	for a in revers_num:
#
# 		if revers_num.index(a) >= min + 1:
# 			num.append(a)
#
# print(num)
# Код из курса

# endregion {===== Основной код =====}
# код из курса
def is_palindrome(num_list):
	reverse_list = []
	for i_num in range(len(num_list) -1, -1, -1):
		reverse_list.append(num_list[i_num])
	if num_list == reverse_list:
		return True
	else:
		return False
nums = list(input('Введите список: '))
new_nums = []
answer = []

for i_nums in range(0, len(nums)):
	for j_elem in range(i_nums, len(nums)):
		new_nums.append(nums[j_elem])
	if is_palindrome(new_nums):
		for i_answer in range(0, i_nums):
			answer.append((nums[i_answer]))
		answer.reverse()
		break
	new_nums = []
print('Исходный список:', nums)
print('Нужно чисел для палиндрома:', len(answer))
print('Список этих чисел:', answer)
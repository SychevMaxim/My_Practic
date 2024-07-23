first_number = int(input('Введите первое число'))
second_number = int(input('Введите второе число'))
third_number = int(input('Введите третье число'))
if first_number == second_number == third_number:
	print('3')
if (first_number == second_number != third_number or second_number == third_number != first_number or third_number ==
	first_number != second_number):
	print("2")
if first_number != second_number != third_number:
	print("0")
def sum_num(counter):
	if counter != num:
		print(counter)
		return sum_num(counter + 1)
	else:
		return num

num = int(input('Введите num'))
print(sum_num(1))
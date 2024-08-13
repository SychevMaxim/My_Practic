def maximum_of_two():
	a = int(input("Введите первое число: "))
	b = int(input("Введите второе число: "))
	if a > b:
		return a
	elif a < b:
		return b
print(maximum_of_two())
def maximum_of_three():

	maximum_two = maximum_of_two()
	c = int(input("введите третье число"))
	if maximum_two < c:
		return c
	else:
		return maximum_two
print(maximum_of_three())
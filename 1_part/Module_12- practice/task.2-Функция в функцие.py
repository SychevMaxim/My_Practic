def positive():
	print("Число положительное")
def negative():
	print("Число отрицательное")
def test():
	n = int(input("Введите число"))
	if n >= 0:
		positive()
	elif n <=0:
		negative()
test()
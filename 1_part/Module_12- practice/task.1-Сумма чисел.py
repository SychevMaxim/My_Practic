def summa_n():
	summ = 0
	n = int(input("Введите число"))
	for number in range(1, n + 1):
		if number <= n:
			summ += number
	print(summ)
summa_n()
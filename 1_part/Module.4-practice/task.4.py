sum = int(input("Введите суму чека: "))
sale = sum * 10 // 100
if sum >= 10000:
	print("ваша скидка состовляет: " , sale)
else:
	print("Ваша скидка состовляет: 0")
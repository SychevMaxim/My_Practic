messenge = input("Ведите сообщение")
numbers = 0
for text in messenge:
	numbers += 1
	if text == "*":
		print("Символ «*» стоит на позиции:", numbers)
		break
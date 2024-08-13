def count_letters():
	text = input("Введите текст: ")
	letter = input("Какую букву ищем? ")
	digit = input("Какое число ищем? ")
	count_letter = 0
	count_number = 0
	for number in text:
		if number == letter:
			count_letter += 1
		elif number == digit:
			count_number += 1
	print("Количество букв", letter + ":", count_letter)
	print("Количество цифр", digit + ":", count_number)
count_letters()
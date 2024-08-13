def rock_paper_scissors():

	first_answer = int(input("Введите: 1- камень 2-ножницы 3-бумага"))

	second_answer = int(input("Введите 1- камень 2-ножницы 3-бумага"))

	if first_answer == second_answer:
		print("Ничья")

	elif first_answer == second_answer - 1 or first_answer == 3 and second_answer == 1:
		print("Первый победил")

	else:
		print("Второй победил")

def guess_the_number():

	secret_number = 7
	answer = int(input("Введите число"))

	if secret_number == answer:
		print("Угадал")

	else:
		print("Не угадал, попробуй еще раз!")

		guess_the_number()

def mainMenu():

	answer = int(input("выберете игру: 1 - Камень ножницы бумага, 2 - Угадай число"))

	if answer == 1:
		rock_paper_scissors()

	elif answer == 2:
		guess_the_number()

	else:
		print("Ошибка ввода")
		mainMenu()
mainMenu()


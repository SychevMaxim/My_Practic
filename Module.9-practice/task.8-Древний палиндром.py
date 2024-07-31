text = input("Введите текст ")
if text == text[::-1]:
	print("Да, Это полиндром")
else:
	print("Нет, это не полиндром")
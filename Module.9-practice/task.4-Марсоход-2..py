vertical = 8
horizontal = 10
answer = ""
while True:
	print("текущие координаты равны:", vertical, horizontal)
	print("в какую сторону вы хотите направить робота: ")
	answer = input("север (клавиша W), юг (клавиша S), запад (клавиша A) или восток (клавиша D) ")
	if vertical == 0:

		if answer == "w":

			vertical += 1
			print(answer)

		elif answer == "d":
			horizontal += 1

		continue

	elif horizontal == 0:

		if answer == "d":
			horizontal += 1

		elif answer == "w":
			vertical += 1

	elif vertical == 15 or horizontal == 20:

		if answer == "s":
			vertical -= 1

		elif answer == "a":
			horizontal -= 1

		continue

	if answer == "w":

		vertical += 1
		print(answer)

	elif answer == "s":
		vertical -= 1

	elif answer == "d":
		horizontal += 1

	elif answer == "a":
		horizontal -= 1

number_rows = int(input("Введите количество рядов"))
number_seats = int(input("введите количество мест"))
place_rows = int(input("Введите место между рядами"))
for number in range(1, number_rows):
	print("=" * number_seats, "*" * place_rows, "=" * number_seats)
start_point = float(input("Введите стартовую амплитуду"))
stop_point = float(input("Введите конечную амплитуду"))
count = 0
while stop_point <= start_point:
	count += 1
	start_point -= 8.4 * (start_point / 100)
print("Маятник считается остановившимся через:", count, "колебаний")
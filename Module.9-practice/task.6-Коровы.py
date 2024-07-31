text = input("Введите строку: ")
milk = 0
cow = 2

for number in text:

	if number == "a":
		milk += cow

	cow += 2

print(milk, "л молока будет воспроизведено за сегодняшний день")
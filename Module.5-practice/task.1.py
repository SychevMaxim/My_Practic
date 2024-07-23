experience = int(input("Ведите количество опыта: "))
level = 1
if experience >= 6000:
	level = 4
elif experience >= 2000:
	level = 3
elif experience >= 1000:
	level = 2
print("Ваш уровень: ", level)
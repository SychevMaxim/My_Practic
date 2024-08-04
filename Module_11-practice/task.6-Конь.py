import math
x_hors = float(input("Введите горизонталь коня"))
y_hors = float(input("введите вертикаль коня"))
x_point = float(input("Введите горизонталь точки"))
y_point = float(input("Введите вертикаль коня"))

x_hors = round(math.floor(10 * x_hors), 1)
y_hors = round(math.floor(10 * y_hors), 1)
x_point = round(math.floor(10 * x_point), 1)
y_point = round(math.floor(10 * y_point), 1)

if (x_point == x_hors + 1 and y_point == y_hors + 2 or x_point == x_hors - 1 and y_point == y_hors + 2 or x_point ==
	x_hors + 2 and y_point == y_hors + 1 or x_point == x_hors + 2 and y_point == y_hors - 1 or x_point == x_hors - 1
	and y_point == y_hors - 4 or x_point == x_hors + 1 and y_point == y_hors - 4 or x_point == x_hors - 4 and y_point
	== y_hors + 1 or x_point == x_hors - 4 and y_point == y_hors - 1):

	print("Конь в точке:", x_hors, y_hors, ".Точка в клетке:", x_point, y_point)
	print("Да, конь может пойти в эту точку!")

else:

	print("Конь в точке:", x_hors, y_hors, ".Точка в клетке:", x_point, y_point)
	print("Нет, конь не может пойти в эту точку!")
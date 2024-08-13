# import math
# x_hors = float(input("Введите горизонталь коня"))
# y_hors = float(input("введите вертикаль коня"))
# x_point = float(input("Введите горизонталь точки"))
# y_point = float(input("Введите вертикаль коня"))
#
# x_hors = round(math.floor(10 * x_hors), 1)
# y_hors = round(math.floor(10 * y_hors), 1)
# x_point = round(math.floor(10 * x_point), 1)
# y_point = round(math.floor(10 * y_point), 1)
#
# if (x_point == x_hors + 1 and y_point == y_hors + 2 or x_point == x_hors - 1 and y_point == y_hors + 2 or x_point ==
# 	x_hors + 2 and y_point == y_hors + 1 or x_point == x_hors + 2 and y_point == y_hors - 1 or x_point == x_hors - 1
# 	and y_point == y_hors - 4 or x_point == x_hors + 1 and y_point == y_hors - 4 or x_point == x_hors - 4 and y_point
# 	== y_hors + 1 or x_point == x_hors - 4 and y_point == y_hors - 1):
#
# 	print("Конь в точке:", x_hors, y_hors, ".Точка в клетке:", x_point, y_point)
# 	print("Да, конь может пойти в эту точку!")
#
# else:
#
# 	print("Конь в точке:", x_hors, y_hors, ".Точка в клетке:", x_point, y_point)
# 	print("Нет, конь не может пойти в эту точку!")
#
#
# region {===== Мой код. =====}

print('Задача 6. Ход конём')


# В рамках разработки шахматного ИИ стоит новая задача.
# По заданным вещественным координатам коня
# и второй точки программа должна определить может ли конь ходить в эту точку.
#
# Используйте как можно меньше конструкций if и логических операторов.
# Обеспечьте контроль ввода.

# Введите местоположение коня:
# 0.071
# 0.118
# Введите местоположение точки на доске:
# 0.213
# 0.068
# Конь в клетке (0, 1). Точка в клетке (2, 0).
# Да, конь может ходить в эту точку.


# РЕШЕНИЕ
# =============================

# Получение данных
print()
x_horse = float(input('Конь по горизонтали: '))
y_horse = float(input('Конь по вертикали: '))

x_point = float(input('Точка по горизонтали: '))
y_point = float(input('Точка по вертикали: '))

# проверяем корректность координат коня
# корректность точки проверять смысла нет
# она будет отсеиваться, если не правильная,
# при расчетах
if 0 < x_horse < 0.8 and 0 < y_horse < 0.8:

    # перезаписываем координаты в удобоваримый вид
    x_horse = int(x_horse * 10)
    y_horse = int(y_horse * 10)

    x_point = int(x_point * 10)
    y_point = int(y_point * 10)

    # выводим координаты коня и точки
    print()
    print(f'Конь в клетке ({x_horse}, {y_horse}). Точка в клетке ({x_point}, {y_point}).')

    # проверяем корректность хода
    if abs(x_point - x_horse) == 2 and abs(y_point - y_horse) == 1:
        print('Да, конь может ходить в эту точку.')
    else:
        print('Нет, конь не может ходить в эту точку.')

else:
    print("Клетки с такой координатой не существует")

# =============================

# endregion {===== Мой код. =====}
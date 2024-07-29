print('\nЗадача task.5-функция. .\n')

# РЕШЕНИЕ
# Перед изучением функций из программирования Саша решил оживить свои знания о функциях математики. Помогите Саше
# написать программу, которая будет считать значение функции в каждой точке отрезка с нужным шагом, начиная с конца).

# Напишите программу, которая получает на вход начало и конец отрезка,
# а также шаг (отрицательный),
# а затем высчитывает функцию y в каждой точке отрезка и выводит ответ на экран с нужным шагом, начиная с конца.
#
# Сама функция выглядит так:
#
# Пример
#
# Введите начало отрезка: −2
#
# Введите конец отрезка: 2
#
# Введите шаг: −1
#
# В точке 2 функция равна 9
#
# В точке 1 функция равна 0
#
# В точке 0 функция равна 1
#
# В точке −1 функция равна 6
#
# В точке −2 функция равна 9
# =============================





# region {===== Основной код =====}

first_number = int(input("Введите начало отрезка "))
second_number = int(input("введите конец отрезка: "))
step = int(input("введите шаг отрезка"))

y = 0

for x in range(first_number, second_number + 1, step):

	y = x**3 + 2 * x ** 2 - 4 * x + 1
	print("В точке", x, "функция ровна", y)

# endregion {===== Основной код =====}
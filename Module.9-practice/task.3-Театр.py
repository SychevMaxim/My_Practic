print('\nЗадача 3. Театр.\n')

# РЕШЕНИЕ
print() # пустая строка

# В городе планируют построить театр под открытым небом, но для начала нужно оценить,
# сколько сделать рядов, сидений в них и каким должно быть расстояние между рядами.

# Что нужно сделать

# Напишите программу, которая получает на вход количество рядов,
# сидений и свободных метров между рядами, а затем выводит примерный макет театра на экран.


# Сцена
# Введите кол-во рядов: 5
# Введите кол-во сидений ряду: 7
# Введите кол-во метров между рядами: 3
#
# ======= *** =======
# ======= *** =======
# ======= *** =======
# ======= *** =======
# ======= *** =======
# =============================





# region {===== Основной код =====}

number_rows = int(input("Введите кол-во рядов: "))
number_seats = int(input("Введите кол-во сидений ряду: "))
interval = int(input("Введите кол-во метров между рядами: "))

for number in range(number_rows):
	print("=" * number_seats, "*" * interval, "=" * number_seats)

# endregion {===== Основной код =====}
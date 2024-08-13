print('\nЗадача Генерация списка. .\n')

# РЕШЕНИЕ
#
# =============================





# region {===== Основной код =====}

N = int(input("Введите число: "))
listing = []

for num in range(1, N + 1, 2):
	listing.append(num)

print("список нечетных чисел от 1 до", str(N) + ":", listing)

# endregion {===== Основной код =====}
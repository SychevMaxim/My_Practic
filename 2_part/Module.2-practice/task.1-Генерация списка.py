print('\nЗадача Генерация списка. .\n')

# РЕШЕНИЕ
# Дано целое число N. Напишите программу, которая формирует список из нечётных чисел от одного до N.
# =============================





# region {===== Основной код =====}

N = int(input("Введите число: "))
result_lst = []

for num in range(1, N + 1, 2):
	result_lst.append(num)

print("список нечетных чисел от 1 до", str(N) + ":", result_lst)
print(f'Cписок нечетных чисел от 1 до {str(N)}: {result_lst}')

# endregion {===== Основной код =====}
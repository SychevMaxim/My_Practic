print('\nЗадача task.3. .\n')

# РЕШЕНИЕ
# Мы всё ближе и ближе подбираемся к серьёзной математике. Одна из классических задач — задача на нахождение
# факториала числа. И в будущем мы с ней ещё встретимся.

# n! = 1 * 2 * 3 * 4 * 5 * … * n
# =============================





# region {===== Основной код =====}

n = int(input("Введите число желаемое возвести в факториал: "))
factorial = 1

for factorial_cicle in range(1, n + 1):
	factorial *= factorial_cicle

print(factorial)

# endregion {===== Основной код =====}
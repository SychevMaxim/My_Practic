print('\nЗадача task.2-Долги. .\n')

# РЕШЕНИЕ
# «МирПрогБанк» наконец-то разделил законопослушных граждан и должников и поместил их в разные базы.
# Но банк не торопится сильно давить на неплательщиков.
# Операторам банка дали задание позвонить каждому пятому должнику из списка (нумерация начинается с нуля) и уточнить,
# какую сумму каждый из них задолжал банку.
#
# Напишите программу, которая получает данные о количестве должников,
# а затем спрашивает у каждого пятого (начиная с нуля) его долг. В конце выводится общая сумма долгов.
# =============================





# region {===== Основной код =====}

debt = 0
count_debt = int(input("Введите количество должников: "))
sum_debt = 0

for number_debt in range(5, count_debt + 5, 5):

	print("Должник с номером:", number_debt)
	debt = int(input("Сколько должны? "))
	sum_debt += debt

print("Общая сума долга составляет:",sum_debt)

# endregion {===== Основной код =====}
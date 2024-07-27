print('\nЗадача task.4. .\n')

# РЕШЕНИЕ
# В классе N человек. Каждый из них получил за урок по информатике оценку: 3, 4 или 5, двоек сегодня не было.
# Напишите программу,
# которая получает список оценок — N чисел — и выводит на экран сообщение о том, кого сегодня больше:
# отличников, хорошистов или троечников.

# Замечание: можно предположить, что количество отличников, хорошистов, троечников различно.
# =============================





# region {===== Основной код =====}

n = int(input("Сколько учеников в классе ? "))

estimation = 0
estimation_3 = 0
estimation_4 = 0
estimation_5 = 0

for count_n in range(n):

	estimation = int(input("что получил ученик"))

	if estimation == 3:
		estimation_3 += 1

	elif estimation == 4:
		estimation_4 += 1

	elif estimation == 5:
		estimation_5 += 1

if estimation_4 == estimation_5 == estimation_3:
	print("Сегодня получили всех оценок поровну!")

elif estimation_4 > estimation_3 and estimation_4 > estimation_5:
	print("Четверок сегодня больше всего!")

elif estimation_3 > estimation_5 and estimation_3 > estimation_4:
	print("Троек сегодня больше всего!")

elif estimation_5 > estimation_4 and estimation_5 > estimation_3:
	print('Пятерок сегодня больше всего')

# endregion {===== Основной код =====}
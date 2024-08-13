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
# оценка
estimation = 0
# оценка 3
estimation_3 = 0
# оценка 4
estimation_4 = 0
# оценка 5
estimation_5 = 0
# повторяется по 1 разу за ученика
for count_estimation in range(n):
	# переменная в которой хранится оценка ученика
	estimation = int(input("что получил ученик"))
	# если оценка 3
	if estimation == 3:
		estimation_3 += 1
	# если оценка 4
	elif estimation == 4:
		estimation_4 += 1
	# если оценка 5
	elif estimation == 5:
		estimation_5 += 1
# если оценок поровну
if estimation_4 == estimation_5 == estimation_3:
	print("Сегодня получили всех оценок поровну!")
# если четверок больше
elif estimation_4 > estimation_3 and estimation_4 > estimation_5:
	print("Четверок сегодня больше всего!")
# если троек больше
elif estimation_3 > estimation_5 and estimation_3 > estimation_4:
	print("Троек сегодня больше всего!")
# если пятерок больше
elif estimation_5 > estimation_4 and estimation_5 > estimation_3:
	print('Пятерок сегодня больше всего')

# endregion {===== Основной код =====}
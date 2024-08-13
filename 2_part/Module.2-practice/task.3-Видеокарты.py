print('\nЗадача Видеокарты. .\n')

# РЕШЕНИЕ
# В базе магазина электроники есть список видеокарт компании NVIDIA разных поколений. Вместо полных названий хранятся
# только числа, которые обозначают модель и поколение видеокарты. Недавно компания выпустила новую линейку видеокарт.
# Самые старшие поколения разобрали за пару дней.

# Напишите программу, которая удаляет наибольшие элементы из списка видеокарт.
# =============================





# region {===== Основной код =====}

count_videoCards = int(input("Количество видеокарт: "))
videoCards = []
newvideoCards = []

for num in range(1, count_videoCards + 1):
	print("Видеокарта", str(num) + ":", end=" ")
	number = int(input())
	videoCards.append(number)

for series in videoCards:

	if series < 3090:
		newvideoCards.append(series)

print("Старый список видеокарт", videoCards)

print("Новый список видео карт", newvideoCards)

# endregion {===== Основной код =====}
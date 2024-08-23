print('\nЗадача Песни. .\n')

# РЕШЕНИЕ
# Напишите программу, которая запрашивает у пользователя количество песен из списка и их названия, а на экран выводит
# общее время их звучания.
# =============================





# region {===== Основной код =====}

violator_songs = [

['World in My Eyes', 4.86],

['Sweetest Perfection', 4.43],

['Personal Jesus', 4.56],

['Halo', 4.9],

['Waiting for the Night', 6.07],

['Enjoy the Silence', 4.20],

['Policy of Truth', 4.76],

['Blue Dress', 4.29],

['Clean', 5.83]

]
count = int(input("введите количество песен "))
full_time = 0

for _ in range(count):

	name = input('Введите название песни ')
	counter = 0

	for _ in range(len(violator_songs)):

		if violator_songs[counter][0] == name:
			full_time += violator_songs[counter][1]

		counter += 1

print(full_time)


# endregion {===== Основной код =====}
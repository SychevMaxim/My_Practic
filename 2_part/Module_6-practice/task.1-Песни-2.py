print('\nЗадача 1.  Песни-2.\n')

# РЕШЕНИЕ
# Напишите программу, которая запрашивает у пользователя количество песен из списка и их названия,
# а на экран выводит общее время их звучания.
#
# Пример
#
# Сколько песен выбрать? 3
#
# Название первой песни: Halo
#
# Название второй песни: Enjoy the Silence
#
# Название третьей песни: Clean
#
# Общее время звучания песен: 14,93 минуты
# =============================





# region {===== Основной код =====}

violator_songs = {
'World in My Eyes': 4.86,
'Sweetest Perfection': 4.43,
'Personal Jesus': 4.56,
'Halo': 4.9,
'Waiting for the Night': 6.07,
'Enjoy the Silence': 4.20,
'Policy of Truth': 4.76,
'Blue Dress': 4.29,
'Clean': 5.83
}
time = 0
count = int(input('Введите количество песен: '))
for counter in range(1, count + 1):
	name = input(f'введите {counter} песню: ')
	if name in violator_songs:
		time += violator_songs[name]
print(f'Общее время прослушивания песен {round(time, 2)}')

# endregion {===== Основной код =====}
print('\nЗадача Кино. .\n')

# РЕШЕНИЕ
# Напишите программу, в которой пользователь вводит фильм. Если кинокартина есть в перечне,
# то добавляется в список любимых. Если её нет, то выводится ошибка. В конце выведите весь список любимых фильмов.
# =============================





# region {===== Основной код =====}

films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия', 'Город грехов', 'Мементо',
		 'Отступники', 'Деревня']
favorit_films = []
count_film = int(input("Введите количество фильмов желаемых добавить"))

for _ in range(count_film):

	name = input("Введите название фильма: ")

	for num in range(len(films)):

		if films[num] == name:
			favorit_films.append(name)
			break
	else:
		print("Ошибка у нас нет такого фильма")


print("Ваши любимые фильмы:", favorit_films)

# endregion {===== Основной код =====}
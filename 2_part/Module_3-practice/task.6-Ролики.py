print('\nЗадача Роллики. .\n')

# РЕШЕНИЕ
# Пользователь вводит два списка размеров: N размеров роликов и K размеров ног людей. Реализуйте код,
# который определяет, какое наибольшее число человек может одновременно взять ролики и пойти кататься.
# =============================





# region {===== Основной код =====}

roll = []
people = []
count_roll = int(input("Введите количество роликов"))
count = 0
counter = 1

for a in range(1, count_roll + 1):

	print("Введите размер", a, "коньков: ", end='')
	size_roll = int(input())
	roll.append(size_roll)

print()
count_people = int(input("Введите количество людей"))

for b in range(1, count_people + 1):

	print("Введите размер", b, "человека: ", end='')
	size_people = int(input())
	people.append(size_people)

print()

for num in range(count_roll - 1):

	for number in range(count_people - 1):

		if roll[num] == people[number]:

			roll.remove(roll[num])
			people.remove(people[number])
			count_roll -= 1
			count_people -= 1
			count += 1

print('Наибольшее количество людей, которые могут взять ролики:', count)

# endregion {===== Основной код =====}
print('\nЗадача Бегущая строка. .\n')

# РЕШЕНИЕ
# Вы пишете программу для маленького табло, в котором циклически повторяется один и тот же текст или числа,
# например как в метро, автобусах или трамваях.

# Дан список из N элементов и целое число K. Напишите программу, которая циклически сдвигает элементы списка вправо на
# K позиций. Используйте минимально возможное количество операций присваивания.
# =============================





# region {===== Основной код =====}

shift = int(input("Введите сдвиг: "))
current_list = input("Введите  список: ")
current_list = list(current_list)

new_list = []

for num in range(1, len(current_list)):

	if num >= shift:
		new_list.append(current_list[num])
for number in range(shift):

	if number < shift:
		new_list.append(current_list[number])

print('Старый список:', current_list)
print('новый список:', new_list)

# endregion {===== Основной код =====}
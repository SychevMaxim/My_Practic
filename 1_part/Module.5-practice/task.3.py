print('\nЗадача task.3. .\n')

# РЕШЕНИЕ
# В университете на факультет кибернетики очень серьёзный конкурс — поступают только сильнейшие,
# первые десять человек из списка.
# Потом среди поступивших определяется, кто будет получать стипендию.
# Для стипендии общий балл при поступлении должен быть не менее 290.
#
# Напишите программу, которая получает на вход место студента в списке и его балл,
# а затем выводит соответствующие сообщения о поступлении и получении стипендии.
# =============================


# region {===== Основной код =====}

place = int(input("Введите ваше место в строке поступающих: "))
ball = int(input("Введите количество балов: "))
if place <= 10:
	print("Поздравляем, вы поступили!")
	if ball >= 290:
		print("Бонусом вам будет начисляться стипендия.")
	else:
		print("Но вам не хватило баллов для стипендии.")
else:
	print("К сожалению, вы не поступили.")

# endregion {===== Основной код =====}
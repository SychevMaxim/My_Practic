print('\nЗадача task.1. .\n')

# РЕШЕНИЕ
#В свободное время Вася любит играть в компьютерные игры. Однажды у него появилась классная идея для сюжета игры. Чтобы воплотить её в жизнь, он начал изучать геймдизайн. Создавать игру он начал с главного героя и его системы прокачки.

#Напишите программу, которая определяет уровень персонажа в компьютерной игре. Пользователь вводит число «очков
# опыта», а программа вычисляет уровень. Новый уровень даётся при достижении 1000, 2500 и 5000 «очков опыта». Начальный уровень равен единице.
# =============================





# region {===== Основной код =====}
experience = int(input("Ведите количество опыта: "))
level = 1
if experience >= 6000:
	level = 4
elif experience >= 2000:
	level = 3
elif experience >= 1000:
	level = 2
print("Ваш уровень: ", level)


# endregion {===== Основной код =====}
print('\nЗадача task.6.\n')

# РЕШЕНИЕ
# Семья из трёх человек устала тесниться в однушке и наконец решила переехать.
# При обсуждении, какую купить квартиру, исходя из предпочтений и семейного бюджета,
# они остановились на двух вариантах:

# Выбрать квартиру попросторнее (не менее 100 м2), но стоимостью не более 10 млн.
# Немного расширить круг поиска, то есть выбрать квартиру поменьше (от 80 м2),
# но и стоимостью не более 7 млн.
# Напишите программу, которая получает на вход стоимость квартиры и её площадь и выводит сообщение, подходит ли она.
# =============================


# region {===== Основной код =====}

s_apportament = int(input("Введите площадь квартиры: "))
price_apportament = int(input("Введите цену квартиры: "))

if (s_apportament >= 100) and (price_apportament <= 10000000):
	print("Квартира подходит!")

elif (s_apportament >= 80) and (price_apportament <= 7000000):
	print("Квартира подходит!")

else:
	print("Квартира не подходит")

# endregion {===== Основной код =====}
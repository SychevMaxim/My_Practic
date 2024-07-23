s_apportament = int(input("Введите площадь квартиры: "))
price_apportament = int(input("Введите цену квартиры: "))
if s_apportament >= 100 and price_apportament <= 10000000:
	print("Квартира подходит!")
elif s_apportament >= 80 and price_apportament <= 7000000:
	print("Квартира подходит!")
else:
	print("Квартира не подходит")
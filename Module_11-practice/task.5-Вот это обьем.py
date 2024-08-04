v_erth = float(1.08321 * 10 ** 12)
random_r = float(input("Введите радиус случайной планеты"))
random_v = float(4/3 * 3.14 * (random_r ** 3))
if random_v > v_erth:
	print("объем планеты больше земли в:", round(random_v / v_erth, 3))
elif random_v < v_erth:
	print("Объем планеты земля больше в:", round(v_erth / random_v, 3))
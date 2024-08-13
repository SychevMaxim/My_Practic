import math

x_count = int(input("ведите количество чисел: "))

for number in range(x_count + 1):

	x = float(input("введите число: "))

	if x >= 0:
		print("x =",  math.ceil(x), "log(x) =", math.log(math.ceil(x)))

	elif x < 0:
		print("x =", math.floor(x), "exp(x) =", math.exp(math.floor(x)))
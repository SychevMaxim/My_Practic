n = float(input("введите число"))
x = n
count = 0
if n >= 1:
	while n > 10:
		count += 1
		n /= 10
	if n < 10:
		print("Формат плавающей точки x =", n, "* 10 **", count)

elif x < 1:
	while x < 1:
		x *= 10
		count += 1
	if x >= 1:
		print("Формат плавающей точки x =", round(x, 7), "* 10 ** -" + str(count))
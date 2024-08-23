print('\nЗадача Страшный код. .\n')

# РЕШЕНИЕ
# Используя знания о методах списков, а также о стиле программирования, помогите другу переписать программу
# =============================





# region {===== Основной код =====}

a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]

counter_three = 0
counter_five = 0
a.extend(b)

for i in a:
	if i == 5:
		a.remove(i)
		counter_five += 1
a.extend(c)
for i in a:
	if i == 3:
		counter_three += 1
print(a)
print('Количество троек',counter_three)
print('количество пятерок', counter_five)

# endregion {===== Основной код =====}
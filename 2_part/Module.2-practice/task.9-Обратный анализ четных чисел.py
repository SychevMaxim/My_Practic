print('\nЗадача Обратный анализ четных чисел. .\n')

# РЕШЕНИЕ
# Напишите программу, которая считывает целые числа из списка и выводит из него только чётные в обратном порядке.
# =============================





# region {===== Основной код =====}

text = input("Введите строку: ")
text = list(text)
count = len(text) - 1
last_text = []

for _ in range(len(text)):

	for num in text[count]:
		count -= 1
		last_text.append(num)

text = []

for number in last_text:

	if int(number) % 2 == 0:
		text.append(number)

print(text)

# endregion {===== Основной код =====}
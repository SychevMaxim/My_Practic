print('\nЗадача 2.Самое длинное слово.\n')

# РЕШЕНИЕ
# Пользователь вводит строку, содержащую пробелы. Найдите в ней самое длинное слово, выведите его и его длину. Если
# таких слов несколько, выведите первое.
# =============================





# region {===== Основной код =====}

string = input('Введите строку: ').split()
counter_letter = 0
max_letter = 0
max_word = ''

for word in string:

	for letter in word:

		if letter != '.':
			counter_letter += 1

	if counter_letter > max_letter:

		max_word = word
		max_letter = counter_letter

	counter_letter = 0

print(f'Самое длинное слово - {max_word}')
print(f'Длина этого слова: {max_letter}')

# endregion {===== Основной код =====}
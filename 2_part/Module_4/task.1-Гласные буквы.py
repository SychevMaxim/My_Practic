print('\nЗадача task.1-Гласные буквы. .\n')

# РЕШЕНИЕ
# Напишите программу, которая запрашивает у пользователя текст и генерирует список гласных букв этого материала (сама
# строка вводится на русском языке). Выведите в консоль сам список и его длину.

# Введите текст: Нужно отнести кольцо в Мордор!

#  Список гласных букв: ['у', 'о', 'о', 'е', 'и', 'о', 'о', 'о', 'о']

#Длина списка: 9
# =============================





# region {===== Основной код =====}
# Гласные:
vowel = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']

# Список для новых гласных
vowel_inText = []

# Строка пользователя
word_lst = list(input('Введите строку'))

# счетчик гласных
counter_vowel = 0

# Прохожу по каждой букве и проверяю гласная ли она
for letter in word_lst:

	for current_vowel in vowel:

		if letter == current_vowel:

			counter_vowel += 1
			vowel_inText.append(letter)

print('количество гласных букв:', counter_vowel)
print('список гласных букв:', vowel_inText)

# endregion {===== Основной код =====}
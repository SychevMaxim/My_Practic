print('\nЗадача task.1-Великий и могучий. .\n')

# РЕШЕНИЕ
# Напишите программу,
# которая получает на вход текст и находит длину самого длинного слова в нём.
# Слова в тексте разделяются одним пробелом.
# =============================





# region {===== Основной код =====}

longWord = 0
lastLongWord = 0
text = input("Введите текст: ")

for letter in text:

	if letter != " ":
		longWord += 1

	if letter == " ":
		longWord = 0

	elif longWord > lastLongWord:
		lastLongWord = longWord

print("Самое длинное слово в тексте:", lastLongWord)


# endregion {===== Основной код =====}
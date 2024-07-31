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

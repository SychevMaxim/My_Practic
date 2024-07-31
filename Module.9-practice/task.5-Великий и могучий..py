longWord = 0
lastLongWord = 0
letter = ''
text = input("Введите текст: ")
for number in text:
	if number != " ":
		longWord += 1
	if number == " ":
		longWord = 0
	elif longWord > lastLongWord:
		lastLongWord = longWord
print("Самое длинное слово в тексте:", lastLongWord)

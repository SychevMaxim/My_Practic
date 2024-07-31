count_word = 0
for wordli in range(10):
	word = input("ведите слово: ")
	if word == "Карамба" or word == "карамба":
		print("Ты прошел")
		count_word += 1
	else:
		print("Ты не прошел")
print("Количество прошедших:", count_word)
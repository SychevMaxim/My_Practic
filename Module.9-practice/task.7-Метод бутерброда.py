word = input("Введите зашифрованное слово")
numberLater = 0
even = ''
notEven = ''
for text in word:
  numberLater += 1
  if numberLater % 2 == 0:
    even += text
  else:
    notEven += text
print(notEven + even[::-1])
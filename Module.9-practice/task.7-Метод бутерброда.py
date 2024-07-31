word = input("Введите зашифрованное слово: ")
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

# region {===== My_Code =====}

# Получение данных

# сохраняем введенное пользователем слово
input_word = input('Введите строку: ')

# перевернутое слово
reverse_word = ''

# переворачиваем введенное слово
for char in input_word:
    reverse_word = char + reverse_word

# проверяем является ли слово палиндромом
if input_word == reverse_word:
    print('Да, это палиндром!')
else:
    print('Нет, это не палиндром!')

# endregion {===== My_Code =====}
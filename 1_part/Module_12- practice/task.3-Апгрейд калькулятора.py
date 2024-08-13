def summ(x):
  sumSum = 0
  for number in range(1, x + 1):
    sumSum += number
  print(sumSum)

def maximum(x):
  last_num = 0
  while x > 0:
    num = x % 10
    x //= 10
    if last_num < num:
      last_num = num
  print(last_num)

def minimum(x):
  last_num = x % 10
  x //= 10
  while x > 0:
    num = x % 10
    x //= 10
    if last_num > num:
      last_num = num
  print(last_num)

x = int(input("Введите число: "))
action = int(input("Введите действие (1 - сумма чисел, 2 - максимальное число, 3 - минимальное число): "))

if action == 1:
  summ(x)
elif action == 2:
  maximum(x)
elif action == 3:
  minimum(x)
else:
  print("Некорректный выбор действия.")
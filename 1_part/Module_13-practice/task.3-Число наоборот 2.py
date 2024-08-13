N = int(input("Введите первое число"))
K = int(input("Введите второе число"))
summ = N + K
print("Сумма:", summ)
revers_n = str(N)[::-1]
revers_k = str(K)[::-1]
revers_sum = int(revers_n) + int(revers_k)
print("Сумма наоборот:", revers_sum)
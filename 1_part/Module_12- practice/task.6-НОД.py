def NOD( a, b):

    if a > b:
        temp = b

    else:
        temp = a

    for number in range(1, temp + 1):

        if((a % number == 0) and(b % number == 0)):
            nod = number

    return nod
x = int(input("Введите первое число") )
y =int(input("введите второе число"))
num = NOD(x, y)
print("Нод этих чисел равен: ")
print(num)

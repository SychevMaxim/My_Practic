passing_score = 270
Rassian_language = int(input("Введите количество баллов по русскому: "))
Mathematic = int(input("Введите количество баллов по математике: "))
Informatic = int(input("Введите количество баллов по информатике: "))
sum_sore = Rassian_language + Mathematic + Informatic
if sum_sore >= passing_score:
    print("Поздравляю, ты поступил на бюджет!")
else:
    print("К сожелению, ты не прошел на бюджет")
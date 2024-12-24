import random

class Person:
    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.food = 50 # Еда у человека, а не в доме
        self.money = 0 # Деньги у человека

    def eat(self):
        if self.food > 0:
            self.fullness += 20
            self.food -= 10
            print(f"{self.name} поел. Сытость: {self.fullness}, Еда: {self.food}")
        else:
            print(f"{self.name} нечего есть!")

    def work(self):
        self.fullness -= 10
        self.money += 25
        print(f"{self.name} поработал. Сытость: {self.fullness}, Деньги: {self.money}")

    def play(self):
        self.fullness -= 5
        print(f"{self.name} поиграл. Сытость: {self.fullness}")

    def go_to_shop(self):
        if self.money >= 10:
            self.food += 20
            self.money -= 10
            print(f"{self.name} сходил в магазин. Еда: {self.food}, Деньги: {self.money}")
        else:
            print(f"{self.name} не хватает денег на еду!")


artem = Person("Максим")

while True:
    print(f"\n--- Состояние {artem.name} ---")
    print(f"Сытость: {artem.fullness}, Еда: {artem.food}, Деньги: {artem.money}")

    print("\nВыберите действие:")
    print("1. Есть")
    print("2. Работать")
    print("3. Играть")
    print("4. Идти в магазин")
    print("0. Закончить симуляцию")

    choice = input("Введите номер действия: ")

    if choice == '1':
        artem.eat()
    elif choice == '2':
        artem.work()
    elif choice == '3':
        artem.play()
    elif choice == '4':
        artem.go_to_shop()
    elif choice == '0':
        break
    else:
        print("Некорректный ввод.")

    if artem.fullness < 0:
        print(f"{artem.name} умер от голода!")
        break


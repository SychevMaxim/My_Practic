print('\nЗадача Считалка. .\n')

# РЕШЕНИЕ
# На вход подаётся количество человек N и номер K. Напишите программу, которая выводит число от 1 до N — это номер
# человека, который останется в кругу последним.
# =============================





# region {===== Основной код =====}

def text(n, k):

    people = list(range(1, n + 1))
    current_index = 0

    while len(people) > 1:
        print(people)
        current_index = (current_index + k - 1) % len(people)
        print("Выбывает человек под номером", people[current_index])
        people.pop(current_index)

    return people[0]

n = int(input("Количество человек: "))
k = int(input("Какое число в считалке? "))


last_person = text(n, k)
print("Остался человек под номером", last_person)

# endregion {===== Основной код =====}
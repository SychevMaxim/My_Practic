print('\nЗадача контейнеры. .\n')

# РЕШЕНИЕ
# Контейнеры на складе лежат в ряд в порядке не возрастания (меньше либо равно) массы в килограммах. На склад привезли
# ещё один контейнер, который тоже нужно положить на определённое место.

# Напишите программу, которая получает на вход невозрастающую последовательность натуральных чисел.
# Они означают массу
# каждого контейнера в ряду. После этого вводится число X — масса нового контейнера.
# Программа выводит номер, под которым будет лежать новый контейнер. Если в ряду есть контейнеры с массой,
# как у нового, то его нужно положить после них.
# =============================


# region {===== MyCode =====}

# # region {===== Переменные =====}
#
# # кол-во контейнеров
# container_count = 0
# # масса контейнера
# weight = 0
# # max масса контейнера
# max_weight = 0
# # индекс контейнера с максимальной массой
# max_index = 0
# # список веса контейнеров
# weight_list = []
#
# # endregion {===== Переменные =====}
#
#
# # region {===== Функции =====}
#
# # region {===== weight_control_func =====}
# def weight_control_func(number):
#     # функция контроля ввода веса контейнеров
#
#     while number > 200:
#         # проверяем вес контейнера
#         # если больше 200, получаем новое значение
#         if number > 200:
#             print('\nОшибка ввода!')
#             print('Введите вес менее 200 кг.')
#             number = int(input('\nВведите вес контейнера: '))
#
#     # возвращаем корректный вес
#     return number
# # endregion {===== weight_control_func =====}
#
# # region {===== find_max_func =====}
#
# def find_max_func(num_list, null_ind):
#     # функция поиска max числа в списке
#     # возвращает max число в списке и индекс
#     # этого числа
#
#     # максимальное число в списке
#     max_num = 0
#     # индекс максимального числа в списке
#     max_ind = null_ind
#
#     # сохраняем в max_num значение
#     # начального индекса поиска
#     max_num = num_list[null_ind]
#     for index in range(null_ind, len(num_list)):
#         if num_list[index] > max_num:
#             max_num = num_list[index]
#             max_ind = index
#     # возвращаем max число и его индекс
#     return max_num, max_ind
#
# # endregion {===== find_max_func =====}
#
# # endregion {===== Функции =====}
#
#
# # region {===== Основной код =====}
#
# # получаем кол-во контейнеров
# container_count = int(input('Количество контейнеров: '))
# print()
#
# # цикл занесения в список веса контейнеров
# for _ in range(container_count):
#     # получаем вес контейнера
#     weight = int(input('Введите вес контейнера: '))
#     # контроль веса
#     weight = weight_control_func(weight)
#     # добавляем вес в список
#     weight_list.append(weight)
#
# # ищем максимальный вес и его индекс в списке
# max_weight, max_index = find_max_func(weight_list, 0)
#
# # меняем местами вес с 0 индексом и мах вес
# weight_list[0], weight_list[max_index] = (
#     weight_list[max_index], weight_list[0])
#
# # цикл сортировки списка
# for i in range(1, len(weight_list)):
#     # ищем мах число и его индекс
#     max_weight, max_index = find_max_func(weight_list, i)
#     # меняем местами значение в списке с индексом i
#     # и значение max_weight
#     weight_list[i], weight_list[max_index] = (
#         weight_list[max_index], weight_list[i])
#
# # Артём, пардон, немного отступлю от задания
# # и выведу для наглядности отсортированный список
# print('\n', weight_list, '\n')
#
# # запрашиваем вес контейнера
# # позицию в списке которого хотим узнать
# weight = int(input('Введите вес нового контейнера: '))
# # контроль веса
# weight = weight_control_func(weight)
#
# # ищем позицию в списке
# for i in range(len(weight_list)):
#     if weight_list[i] >= weight > weight_list[i + 1]:
#         print('Номер, который получит новый контейнер:', (i + 2))
#
# # endregion {===== Основной код =====}

# endregion {===== MyCode =====}


# region {===== Основной код =====}

count_container = int(input("Введите количество контейнеров"))
container_lst = []

for _ in range(count_container):

	current_container = int(input("Введите вес контейнера: "))
	container_lst.append(current_container)

place = 1
new_container = int(input("Введите вес нового контейнера: "))

for num in container_lst:

	if new_container <= num:
		place += 1

print('Место которое будет занимать новый контейнер(с верху):', place)

# endregion {===== Основной код =====}
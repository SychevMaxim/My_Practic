print('\nЗадача 1. Ревью кода.\n')

# РЕШЕНИЕ
# Перепишите этот код так, чтобы он был максимально pythonic и Ваня мало к чему мог придраться (только если очень
# захочется). Убедитесь, что программа верно работает. П
# роверки на существование записей в словаре не обязательны, но приветствуются.

# Результат работы программы:
#
# Список пар «ID студента — возраст»: [(1, 23), (2, 24), (3, 22)]
#
# Полный список интересов всех студентов:
# {'running', 'computer games', 'math', 'languages', 'biology, swimming', 'health food'}
#
# Общая длина всех фамилий студентов: 20
# =============================





# region {===== Основной код =====}

students = {
1: {
'name': 'Bob',
'surname': 'Vazovski',
'age': 23,
'interests': ['biology, swimming']
},
2: {
'name': 'Rob',
'surname': 'Stepanov',
'age': 24,
'interests': ['math', 'computer games', 'running']
},
3: {
'name': 'Alexander',
'surname': 'Krug',
'age': 22,
'interests': ['languages', 'health food']
}
}

counter = 0
lst_hobby = {}
age_index = []
long_surname = 0
lst_hobby['hobby'] = []
for i_keys in students.keys():
	age_index.append((i_keys, students[i_keys]['age']))
	lst_hobby['hobby'] += students[i_keys]['interests']
	long_surname += len(students[i_keys]['surname'])
print(f'Список пар «ID студента — возраст»: {age_index}')
print()
print(f'Полный список интересов всех студентов: {lst_hobby['hobby']}')
print()
print(f'Общая длина всех фамилий студентов: {long_surname}')
# region {===== Изначальный код =====}

# def f(dict):
#
# string = ''
# for i in dict:
# lst += (dict[i]['interests'])
# string += dict[i]['surname']
# cnt = 0
# for s in string:
# cnt += 1
# return lst, cnt
#
# pairs = []
# for i in students:
# pairs += (i, students[i]['age'])
#
# my_lst = f(students)[0]
# l = f(students)[1]
# print(my_lst, l)

# endregion {===== Изначальный код =====}


# endregion {===== Основной код =====}
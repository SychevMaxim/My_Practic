print('\nЗадача 7. Три списка.\n')

# РЕШЕНИЕ
# Нужно выполнить две задачи:

# найти элементы, которые есть в каждом списке;
# найти элементы из первого списка, которых нет во втором и третьем списках.
# Каждую задачу нужно выполнить двумя способами:
#
# без использования множеств;
# с использованием множеств.
# =============================





# region {===== Основной код =====}

array_1 = [1, 5, 10, 20, 40, 80, 100]

array_2 = [6, 7, 20, 80, 100]

array_3 = [3, 4, 15, 20, 30, 70, 80, 120]
print('Решение без использования множеств:')
notin = []
in_team = {}
not_inTeam = {}
for letter in array_1:
	if letter in array_2 and letter in array_3:
		print(letter, end=' ')
		in_team[letter] = letter
	if not letter in array_2 and not letter in array_3:
		not_inTeam[letter] = letter
		notin.append(letter)

print(end='\n')
print(notin)

print('Решение c использования множеств:')
print([letter for letter in in_team])
print([letter for letter in not_inTeam])

# endregion {===== Основной код =====}
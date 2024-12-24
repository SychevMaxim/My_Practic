class parrents():
	name = 'a'
	age = 21
	about = 'jidjjujdjdjdjdjdjdjdjdjdjdjdjdjj'

class childrens():
	first_children = {
		'name': 'b',
		'condition': 'Спокойствие',
		"hunger": 'Сыт',
		'age': 5
	}
	second_children = {
		'name': 'c',
		'condition': 'Стресс',
		"hunger": 'голоден',
		'age': 4
	}

while True:
	activity = int(input('1- информация о родителях, 2 - успокоить ребенка, 3 - покормить ребенка'))
	if activity == 1:
		print(parrents.name, parrents.age, parrents.about)
	elif activity == 2:
		if input("какого ребенка (1,2)?") == 1:
			childrens.first_children['condition'] = 'спокойствие'
		else:
			childrens.second_children['condition'] = 'спокойствие'
	elif activity == 3:
		if input("какого ребенка (1,2)?") == 1:
			childrens.first_children['hunger'] = 'Сыт'
		else:
			childrens.second_children['hunger'] = 'Сыт'
	else:
		print('Ошибка ввода')
	print('информация о первом ребенке')
	for a in childrens.first_children.items():
		print('\n', a)
	print('\n информация о втором ребенке')
	for b in childrens.second_children.items():
		print('\n', b)
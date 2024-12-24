class watter():
	first_element = 'watter'
	def __add__(self, other):
		if other == 'fire':
			return 'steam'
		elif other == 'air':
			return 'storm'
		elif other == 'erth':
			return 'dirt'

class fire:
	first_element = 'fire'
	def __add__(self, other):
		if other == 'watter':
			return 'steam'
		elif other == 'air':
			return 'lighting'
		elif other == 'erth':
			return 'lava'

class air:
	first_element = 'air'
	def __add__(self, other):
		if other == 'watter':
			return 'storm'
		elif other == 'fire':
			return 'lighting'
		elif other == 'erth':
			return 'dust'

class erth:
	first_element = 'erth'
	def __add__(self, other):
		if other == 'watter':
			return 'dirt'
		elif other == 'fire':
			return 'lava'
		elif other == 'air':
			return 'dust'


first_element = input('Введите первый элемент: ')
second_element = input('Введите второй элемент: ')


if first_element == 'watter':
	print('Новый элемент: ', watter.__add__(first_element, second_element))

elif first_element == 'fire':
	print('Новый элемент: ', fire.__add__(first_element, second_element))

elif first_element == 'air':
	print('Новый элемент: ', air.__add__(first_element, second_element))

elif first_element == 'erth':
	print('Новый элемент: ', erth.__add__(first_element, second_element))

def  presence_depth(depth):
	if depth == 'y':
		return input('Введите максимальную глубину: ')
	else:
		return (:)
def value_key(site, key, depth):
	if key in site.value:
		print('значение:', key[:depth] in site.value)
	else:
		if key in site['html']:
			print('значение ', site['html'][])





site = {
	'html': {
		'head': {
			'title': 'Мой сайт'
		},
		'body': {
			'h2': 'Здесь будет мой заголовок',
			'div': 'Тут, наверное, какой-то блок',
			'p': 'А вот здесь новый абзац'
	}
	}
	}
key = input('введите искомый ключ:')
tiefe = input('Хотите ввести максимальную глубину? Y/N:')
def is_prime(name):
	site = {
		'html': {
			'head': {
				'title': f'Куплю/продам {name} недорого'
			},
			'body': {
				'h2': f'У нас самая низкая цена на {name}',
				'div': 'Купить',
				'p': 'Продать'
	}
	}
	}

	return str(site)
count = int(input('Введите количество продуктов'))
site = {}
for _ in range(count):
	name = input('Введите название товара')
	site[name] = is_prime(name)
	print(site)
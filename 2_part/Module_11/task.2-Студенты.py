class student:
	name = 'Ваня Иванов'
	number_grope = 1
	grade = 20

	def __init__(self, name, number_grop, grade):
		self.name = input('Имя: ')
		self.number_grope = input('Номер группы: ')
		self.grade = input('Успеваемость в балах (1-50): ')

for _ in range(10):
	name = input('Имя: ')
	number_grope = input('Номер группы: ')
	grade = input('Успеваемость в балах (1-50): ')
	student()
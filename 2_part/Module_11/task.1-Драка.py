import random
class first_voin:
	helth = 100

class second_voin:
	helth = 100
while True :
	if first_voin.helth == 0 or second_voin.helth ==0:
		break
	else:
		number = random.randint(1, 2)
		if number == 1:
			second_voin.helth -= 20
		elif number == 2:
			first_voin.helth -= 20
		print('атакует воин под номером:', number)
		print('\nздоровье первого война:', first_voin.helth)
		print('здоровье второго война:', second_voin.helth, '\n')
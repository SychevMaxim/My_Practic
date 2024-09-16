def sub_summ(name, summ = 0, full_name = []):
	if isinstance(name, list):
		for letter in name:
			if letter != []:
				if isinstance(letter, list):
					return sub_summ(letter, summ, name)
				else:
					summ += letter
					name.remove(letter)
					return sub_summ(full_name, summ, full_name)
			else:
				name.remove(letter)
				return sub_summ(name, summ, name)
	else:
		summ += int(name)
	return summ
def summ(name, summ):
	if isinstance(name, list):
		for letter in name:
			summ += sub_summ(name)
	return summ
print(summ([[1, 2, [3]], [1], 3, [2]], 0))
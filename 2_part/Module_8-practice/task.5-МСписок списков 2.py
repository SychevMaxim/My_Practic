def sub_list(name, summ_dict, full_name):
	if isinstance(name, list):
		for letter in name:
			if letter != []:
				if isinstance(letter, list):
					return sub_list(letter, summ_dict, name)
				else:
					summ_dict.append(letter)
					name.remove(letter)
					return sub_list(full_name, summ_dict, full_name)
	else:
		return summ_dict
def listt(name, summ_dict = [], full_name = []):
	for letter in name:
		if isinstance(letter, list):
			summ_dict.append(sub_list(letter, summ_dict, letter))
		else:
			summ_dict.append(letter)
	return summ_dict
lst = []
for letter in listt([1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]], [[11, 12, 13], [14, 15], [16, 17, 18]]]):
	if letter != None:
		lst.append(letter)
print(lst)
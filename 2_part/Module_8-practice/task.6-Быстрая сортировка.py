def sub_sorted(name, min_lst, mid_lst, max_lst):
	for letter in name:
		if letter < name[len(name) - 1]:
			min_lst.append(letter)
		elif letter > name[len(name) -1]:
			max_lst.append(letter)
		else:
			mid_lst.append(letter)
	return min_lst, mid_lst, max_lst
def sorted(name, full_lst = []):
	for letter in sub_sorted(name, [], [], []):
		full_lst.extend(sub_sorted(letter, [], [], []))
	return full_lst
full_lst = []
for letter in sorted([5, 2, 4, 1, 3]):
	if letter != []:
		full_lst.append(letter)
print(full_lst)
count_fail = int(input("Введите количество чисел"))
spead = int(input("Введите "))
second = 1

for spead_download in range (spead, count_fail + spead, spead):
	procent = float(spead_download 	/ (count_fail / 100))

	if spead_download <= count_fail:
		print("прошло", second, "секунд. Скачано", spead_download, "из", count_fail, int(procent), "%")
		second += 1

	elif spead_download >= count_fail:
		print("прошло", second, "секунд. Скачано", count_fail, "из", count_fail, "100%")
		print('Загрузка завершена')

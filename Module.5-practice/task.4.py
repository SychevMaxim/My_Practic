print('\nЗадача task.4. .\n')

# РЕШЕНИЕ
# Папа-программист настолько обленился, что вместо того, чтобы спросить у сына, какую оценку тот получил в школе, он написал программу:
#
# rating = int(input('Что получил по математике? '))
# if rating == 2:
#  print('Плохо. Марш учиться!')
# if rating == 3:
#  print('Плохо. Марш учиться!')
# if rating == 4:
#  print('Молодец! Можешь отдохнуть.')
# if rating == 5:
#  print('Молодец! Можешь отдохнуть.')
# Сын посмотрел на код программы и понял, что её можно улучшить. Он даже рассказал папе, как это сделать, за что получил безграничное уважение отца.
#
# Скопируйте программу в редактор и оптимизируйте:
#
# При плохой оценке (2 или 3) выводится сообщение: «Плохо. Марш учиться!»
# При хорошей оценке (4 или 5) выводится сообщение: «Молодец! Можешь отдохнуть».
# В программе не должно быть повторяющихся строк.
# =============================





# region {===== Основной код =====}

rating = int(input('Что получил по математике? '))
if rating == 2 or rating == 3:
 print('Плохо. Марш учиться!')
if rating == 4 or rating == 5:
 print('Молодец! Можешь отдохнуть.')

# endregion {===== Основной код =====}
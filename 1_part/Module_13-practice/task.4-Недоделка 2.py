# def count_number():
# 	number = int(input("Введите число"))
# 	count_number = 0
# 	while number >= 0:
# 		number /= 10
# 		count_number += 1
# 		if number < 1:
# 			break
# 	print(count_number)
# def change_number():
def get_digit_count(number):
  """
  Возвращает количество цифр в числе.

  Args:
      number: Целое число.

  Returns:
      Количество цифр в числе.
  """
  count = 0
  temp = number
  while temp > 0:
    count += 1
    temp = temp // 10
  return count

def swap_first_and_last_digits(number, digit_count):
  """
  Меняет местами первую и последнюю цифры числа.

  Args:
      number: Целое число.
      digit_count: Количество цифр в числе.

  Returns:
      Изменённое число.
  """
  last_digit = number % 10
  first_digit = number // 10 ** (digit_count - 1)
  between_digits = number % 10 ** (digit_count - 1) // 10
  return last_digit * 10 ** (digit_count - 1) + between_digits * 10 + first_digit

def main():
  """
  Основная функция программы.
  """
  first_n = int(input("Введите первое число: "))
  first_num_count = get_digit_count(first_n)

  if first_num_count < 3:
    print("В первом числе меньше трёх цифр.")
  else:
    first_n = swap_first_and_last_digits(first_n, first_num_count)
    print('Изменённое первое число:', first_n)

  second_n = int(input("\nВведите второе число: "))
  second_num_count = get_digit_count(second_n)

  if second_num_count < 4:
    print("Во втором числе меньше четырёх цифр.")
  else:
    second_n = swap_first_and_last_digits(second_n, second_num_count)
    print('Изменённое второе число:', second_n)
    print('\nСумма чисел:', first_n + second_n)


main()
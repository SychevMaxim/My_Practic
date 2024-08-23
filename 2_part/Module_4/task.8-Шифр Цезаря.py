print('\nЗадача 8.Шифр цезаря.\n')

# РЕШЕНИЕ
# Пользователь вводит сообщение и значение сдвига. Напишите программу, которая изменит фразу при помощи шифра Цезаря.

# Пример:
#
# Введите сообщение: это питон.
#
# Введите сдвиг: 3
#
# Зашифрованное сообщение: ахс тлхср.
# =============================





# region {===== Основной код =====}

def caesar_cipher(string, user_shift):
	# иду по алфавиту, беру остаток от 33 чтобы индекс не вышел за границу алфавита
	char_list = [(alphabet[(alphabet.index(sym) + user_shift) % 33] if sym != ' ' else ' ') for sym in string]
	new_str = ''
	for i_char in char_list:
		new_str += i_char
	return new_str
alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
input_str = input('Введите строку: ')
shift = int(input('Введите сдвиг'))

output_str = caesar_cipher(input_str, shift)

# endregion {===== Основной код =====}



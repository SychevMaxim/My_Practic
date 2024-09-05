print('\nЗадача 3. Товары.\n')

# РЕШЕНИЕ
# Напишите программу, которая рассчитывает общую стоимость позиций для каждого товара на складе и выводит эту
# информацию на экран.

# Результат работы программы:
#
# Лампа — 27 штук, стоимость 1134 рубля.
#
# Стол — 54 штуки, стоимость 27 860 рублей.
#
# Диван — 3 штуки, стоимость 3550 рублей.
#
# Стул — 105 штук, стоимость 10 311 рублей.
# =============================





# region {===== Основной код =====}

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

for good_name, good_code in goods.items():
    total_quantity = 0
    total_cost = 0
    for item in store[good_code]:
        total_quantity += item['quantity']
        total_cost += item['quantity'] * item['price']
    print(f"{good_name} — {total_quantity} штук, стоимость {total_cost} рублей.")

# endregion {===== Основной код =====}
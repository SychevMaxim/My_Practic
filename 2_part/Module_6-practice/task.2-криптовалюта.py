print('\nЗадача . Криптовалюта.\n')

# РЕШЕНИЕ
# Напишите программу, которая выполняет следующий алгоритм действий:

# Вывести списки ключей и значений словаря.
# В ETH добавить ключ total_diff со значением 100.
# Внутри fst_token_info значение ключа name поменять с fdf на doge.
# Удалить total_out из словарей внутри списка tokens и присвоить сумму этих значений в total_out внутри ETH.
# Внутри sec_token_info изменить название ключа price на total_price
# =============================





# region {===== Основной код =====}

data = {
"address": "0x544444444444",
"ETH": {
"balance": 444,
"totalIn": 444,
"totalOut": 4,
'summ': 0
},
"count_txs": 2,
"tokens": [
{
"fst_token_info": {
"address": "0x44444",
"name": "fdf",
"decimals": 0,
"symbol": "dsfdsf",
"total_supply": "3228562189",
"owner": "0x44444",
"last_updated": 1519022607901,
"issuances_count": 0,
"holders_count": 137528,
"price": False
},
"balance": 5000,
"totalIn": 0,
"total_out": 0
},
{
"sec_token_info": {
"address": "0x44444",
"name": "ggg",
"decimals": "2",
"symbol": "fff",
"total_supply": "250000000000",
"owner": "0x44444",
"last_updated": 1520452201,
"issuances_count": 0,
"holders_count": 20707,
"price": False
},
"balance": 500,
"totalIn": 0,
"total_out": 0
}
]
}
print('ключи: ', data['address'], data["tokens"][0]["fst_token_info"]['address'], data['tokens'][1]["sec_token_info"][
	'address'])
data['ETH'].update(total_dif = 100)
data['tokens'][0]['fst_token_info']['name'] = 'dodge'
if 'total_out' in ['ETH']:
	print('yes')
print(data['ETH'])

# endregion {===== Основной код =====}
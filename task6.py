inventory_tuple_list = []
while True:
    inventory_tuple_list.append(
        (input('Введите номер товара: '),
                dict({'название': input('Введите название: '),
                'цена': input('Введите цену: '),
                'количество': input('Введите количество: '),
                'eд': input('Введите единцы измерения: '),
            }))
        )
    if input('Товар добавлен. Добавить еще один товар? (да/нет): ') == 'нет':
        break

for ind, el in enumerate(inventory_tuple_list, 1):
    print('Текущая база товаров: ', ind, el)
print(inventory_tuple_list)

output_dict = dict({})
for product in inventory_tuple_list:
    for key, value in product[-1].items():
        if key in output_dict:
            if value not in output_dict.get(key):
                output_dict.get(key).append(value)
        else:
            output_dict.update({key: [value]})
print(f'собрана аналитика: {output_dict}')
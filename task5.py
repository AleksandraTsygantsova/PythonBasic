def_list = [9, 8, 7, 5, 5, 4, 3]
print(def_list)
def_list.append(int(input('Введите новый элемент рейтинга: ')))
print(f'теперь список такой:{sorted(def_list, reverse=True)}')
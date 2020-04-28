fr_list = [input('Введите первый элемент списка: '), input('Введите второй элемент списка: '),
           input('Введите третий элемент списка: '), input('Введите четвертый элемент списка: ')]
print('Вид исходного списка: ', fr_list)
fr_list.insert(0, fr_list.pop(1))
fr_list.insert(2, fr_list.pop(3))
print('Текущий вид списка: ', fr_list)
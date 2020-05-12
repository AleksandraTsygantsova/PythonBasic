def my_div(arg_1, arg_2):
    try:
        return print(arg_1 / arg_2)
    except ZeroDivisionError as e:
        print('Знаменатель не может быть равен нулю')

my_div(int(input('Введите числитель: ')), int(input('Введите знаменатель: ')))

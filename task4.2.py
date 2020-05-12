def my_func(x, y):
    n = 1
    result = 1 / x
    while n < abs(y):
        result = result * (1 / x)
        n += 1
    return print(result)

my_func(int(input('Введите действительное положительное число: ')),
              int(input('Введите целое отрицательное число: ')))
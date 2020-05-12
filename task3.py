def my_func(arg1, arg2, arg3):
      return print(arg1 + arg2 + arg3 - min(arg1, arg2, arg3))

my_func(float(input('Введите первое число: ')),
        float(input('Введите второе число: ')),
        float(input('Введите третье число: ')))
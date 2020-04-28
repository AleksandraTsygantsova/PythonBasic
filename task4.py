user_list = (input('Введите несколько слов через пробел: ').split(' '))
for ind, content in enumerate(user_list, 1):
    print(ind, content[0:10])
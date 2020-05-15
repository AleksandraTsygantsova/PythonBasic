from itertools import count

for el in count(int(input('Введите целое число: '))):
    if el > 15:
        break
    else:
        print(el)

from itertools import cycle
i = 0
for el in cycle(input('Введите последовательность символов: ')):
    if i > 15:
        break
    print(el)
    i += 1
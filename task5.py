from functools import reduce
new_list = [el for el in range(99, 1001) if el % 2 == 0]
print(reduce((lambda x, y: x * y), new_list))
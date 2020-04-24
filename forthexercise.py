user_var = int(input('Введите целое положительное число:'))
max_number = user_var % 10
user_var = user_var // 10

while user_var > 0:
    if max_number < user_var % 10:
        max_number = user_var % 10
        user_var = user_var // 10
print(f'Самая большая цифра в числе: {max_number}')
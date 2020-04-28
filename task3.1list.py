month = int(input('Введите номер месяца (от 1 до 12): '))
season = ['зима', 'весна', 'лето', 'осень']
if month in (1, 2, 12):
    print('Это', season[0])
elif month in (3, 4, 5):
    print('Это', season[1])
elif month in (6, 7, 8):
    print('Это', season[2])
elif month in (9, 10, 11):
    print('Это', season[3])
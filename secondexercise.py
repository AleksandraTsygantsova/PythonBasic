usertime = int(input('Введите время в секундах: '))
time_hours = usertime // 3600
time_minuts = (usertime % 3600) // 60
time_seconds = (usertime % 60)
print(time_hours, 'чч :', time_minuts, 'мм :', time_seconds, 'сс')
def user(**kwargs):
    return print(kwargs)

user(name=input('Имя: '),
    surname=input('Фамилия: '),
    year=input('Год Рождения: '),
    city=input('Город проживания: '),
    email=input('email: '),
    phone=input('phone: '))
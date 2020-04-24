user_revenue = int(input('Введите сумму вашей выручки: '))
user_cost = int(input('Введите сумму ваших издержек: '))
if user_revenue > user_cost:
   print('Ваша выручка больше издержек')
   margin = (user_revenue - user_cost) / (user_revenue) * 100
   print(f'Рентабельность составляет: {margin} %')
   count_of_empl = int(input('Введите численность сотрудников вашей фирмы: '))
   margin_per_unit = (user_revenue - user_cost) / count_of_empl
   print(f'Прибыль в расчете на одного сотрудника составляет {margin_per_unit} руб.')
else:
   print('Ваши издержки больше выручки')
f = open("task3.txt", encoding='utf-8')
lines = f.readlines()
salary_sum = 0
surname_sum = 0
for row in lines:
    line = row.split()
    salary_sum += float(line[1])
    surname_sum += 1
    if (float(line[1]) < 20000):
        print(f'{line[0]} имеет оклад менее 20 000 руб.')

average_salary = salary_sum / surname_sum
print(f'Средний оклад равен: {round(average_salary)} руб')

f.close()
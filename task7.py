import json
result = []
profit = {}
average = []

with open("task7.txt", 'r', encoding='utf-8') as file_read:
    counter = 1
    while True:
        line = file_read.readline().split()

        if not line:
            break

        profit[line[0]] = float(line[-2]) - float(line[-1])

        if profit[line[0]] > 0:
            average.append(profit[line[0]])

        counter += 1


result = [profit, {'average_profit': sum(average) / len(average)}]

with open("task7.2.txt", 'w', encoding='utf-8') as file_write:
    json.dump(result, file_write)
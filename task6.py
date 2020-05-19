f = open("task6.txt", encoding='utf-8')

counter_lines = 0
while True:
    content = f.readline().split()
    sum_el = 0
    n = 0
    while n < (len(content) - 1):
        element = int((content[n + 1].split('('))[0])
        sum_el += element
        n += 1

    dict = {content[0]: sum_el}
    print(dict)

    if len(content) == 0: break
    counter_lines += 1

f.close()

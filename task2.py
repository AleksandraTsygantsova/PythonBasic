f = open("task2.txt", encoding='utf-8')
counter_lines = 0
counter_words = 0

while True:
    content = f.readline()
    if len(content) == 0: break
    counter_lines += 1
    counter_words += len(content.split())

f.close()
print(f'Кол-во строк в файле = {counter_lines}, Кол-во слов в файле = {counter_words}')
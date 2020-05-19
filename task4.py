f = open("task4.txt", encoding='utf-8')
content = f.readlines()
dict = {'One': 'один', 'Two': 'два', 'Three': 'три', 'Four': 'четыре'}
f.close()

f_new = open("task4_2.txt", 'w', encoding='utf-8')

for line in content:
    row = line.split()
    row[0] = dict[row[0]]
    line = ''.join(row)
    f_new.writelines(line+'\n')

f_new.close()

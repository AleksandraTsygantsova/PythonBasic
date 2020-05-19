f = open("task1.txt", 'w')
while True:
    new_content = input('Введите значение новой строки (для выхода введите пробел): ')
    if new_content == ' ': break
    f.write(new_content+'\n')
f.close()
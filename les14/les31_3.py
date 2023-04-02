import os

# 1
# В файле, в одну строку записаны слова и числа через пробел или _
# найти сумму всех чисел.
with open('123.txt', 'r') as f:
    print(sum([int(i) for i in f.read().split(' ' or '_') if i.isdigit()]))

# 2
# Файл содержит числа и буквы. Каждый записан в отдельной строке.
# Нужно считать содержимое в список так, чтобы сначала шли числа по
# возрастанию, а потом слова по возрастанию их длины.
with open('123.txt', 'r') as f:
    f = f.read().split('\n')
    list_alp = list()
    list_dig = list()
    for i in f:
        print(i)
        if i.isalpha():
            list_alp.append(i)
        elif i.isdigit():
            list_dig.append(int(i))
    list_alp.sort(key=len)
    list_dig.sort()
    list_dig.extend(list_alp)
    print(list_dig)

# 3
# Создать текстовый файл, записать в него построчно данные, которые
# вводит пользователь. Окончанием ввода пусть служит пустая строка.
f = open('number3.txt', 'w+')
while True:
    str_ = input('ввод: ')
    if str_ == '':
        break
    f.write(str_ + '\n')
f.close()

# 4
# В текстовом файле посчитать количество строк, а также для каждой
# отдельной строки определить количество в ней символов.
with open('number3.txt') as num:
    length = 0
    dictionary = dict()
    for i in num:
        length += 1
        dictionary[length] = len(i[:-1])
    print(len(dictionary), dictionary, sep='\n')

# 5
# Есть массив состоящий из слов и чисел, нужно записать в
# файл сначала слова в порядке их длины, а после слов
# цифры в порядке возрастания
sub = ['sdas', 23, 'dsa', 93, 'dsddddd', 1, 3, 444]
sub_int = list()
sub_str = list()
for i in sub:
    if isinstance(i, int):
        sub_int.append(i)
    else:
        sub_str.append(i)
sub_int.sort()
sub_str.sort(key=len)
sub_str.extend(sub_int)
print(sub_str)

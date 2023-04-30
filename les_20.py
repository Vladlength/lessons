# 1. Напишите генератор, который на вход получает список чисел и возвращает только те числа,
# которые делятся на 3 без остатка.

list_o = [1, 2, 3, 4, 6, 9, 7, 8, 12]


def gener(list_obj):
    for i in list_obj:
        if i % 3 == 0:
            yield i


a = [i for i in gener(list_o)]
print(a)


# 2. Напишите итератор, который на вход получает строку и возвращает каждый второй символ этой строки.
class Iterator:

    def __init__(self, str_obj):
        self.str_obj = str_obj

    def __iter__(self):
        self.i = 1
        return self

    def __next__(self):
        if self.i < len(self.str_obj):
            res = self.str_obj[self.i]
            self.i += 2
            return res
        else:
            raise StopIteration


a = Iterator('дядя вася')

sub = [i for i in a]
print(sub)


# 3. Напишите генератор, который на вход получает два списка чисел и возвращает только те числа,
# которые есть в обоих списках.

def generator_funk(list1, list2):
    res_set = set(list1) & set(list2)
    for i in res_set:
        yield i


list1 = [1, 2, 3, 4, 5, 6]
list2 = [6, 4, 12, 2, 10]
a = [i for i in generator_funk(list1, list2)]
print(a)


# 4. Напишите генератор, который на вход получает список строк и возвращает только те строки,
# которые содержат букву "a".

def generator_funk(str_list):
    for i in str_list:
        if 'a' in i:
            yield i


str_list = ['sada', 'fdg', 'ads', 'fgfruy', 'gdh']

a = [i for i in generator_funk(str_list)]
print(a)


# 5. Напишите итератор, который на вход получает список чисел и возвращает каждый третий элемент этого списка.

class Iterator:

    def __init__(self, list_obj):
        self.list_obj = list_obj

    def __iter__(self):
        self.i = 2
        return self

    def __next__(self):
        if self.i >= len(self.list_obj):
            raise StopIteration
        res = self.list_obj[self.i]
        self.i += 3
        return res


a = Iterator([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

print([i for i in a])

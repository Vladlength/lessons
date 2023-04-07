import json
from pprint import pprint

with open('diction.json', 'w', encoding='UTF-8') as file:
    sub = list()
    while True:
        el = input('Введите название продукта (чтобы закончить введите "стоп"): ')
        if el == 'стоп':
            break
        cost = int(input('Введите стоимость: '))
        sub.append({'название': el, 'стоимость': cost})
    json.dump(sub, file, ensure_ascii=False, indent=2)

with open('diction.json', 'r', encoding='UTF-8') as file:
    sub = []
    g = json.load(file)
    for i in g:
        a, b = i.values()
        sub.append(b)
    print(sum(sub))


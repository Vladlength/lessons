import time
import requests
from bs4 import BeautifulSoup as BS
import csv
import json


# 49 seconds

def get_html(url):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/111.0.0.0 Safari/537.36 OPR/97.0.0.0'
    }
    req = requests.get(url, headers=headers)
    return req


def parce(html):
    dict_parcer = dict()
    soup = BS(get_html(html).text, 'lxml')
    link_catalog = soup.find_all('div', 'listing-item')
    list_link = ['https://cars.av.by' + i.a.attrs['href'] for i in link_catalog]
    price_catalog_byn = soup.find_all('div', "listing-item__price")
    list_price_byn = [int(i.text.encode('ascii', errors='ignore').decode('UTF-8')[:-1]) for i in price_catalog_byn]
    '''
    > Получаем строку с неразрывным пробелом
    > Далее энкодим в ASCII
    > А после декодим обратно в UTF-8
    Тут главное будет указать параметр errors = ignore. Суть будет в том, что при попытке конвертации в ASCII
    символы nbsp не смогут конвертироваться, из-за того, что их попросту нет в Аски) мы игнорим ошибки,
    связанные с кодировкой, а после уже получившуюся строку фигачим в ютф. 
    В итоге получается чистая строка без лишних символов, а в нашем случае чистая цена. 
    Останется лишь убрать оставшиеся лишние символы - точку.
'''
    price_catalog_usd = soup.find_all('div', "listing-item__priceusd")
    list_price_usd = [int(i.text.encode('ascii', errors='ignore').decode('UTF-8')[:-1]) for i in price_catalog_usd]

    params_catalog = soup.find_all('div', "listing-item__params")
    list_params = [i.text.replace('\xa0', '') for i in params_catalog]

    for i in range(len(list_link)):
        elements_params = list_params[i].split(', ')
        dict_parcer[list_link[i]] = [list_price_byn[i],
                                     list_price_usd[i],
                                     elements_params[0][:elements_params[0].index('.')],
                                     elements_params[1]
                                     ]
        try:
            dict_parcer[list_link[i]].extend([elements_params[2],
                                              elements_params[3].encode('ascii', errors='ignore').decode('CP1251')])
        except:
            dict_parcer[list_link[i]].extend([' ',
                                              elements_params[2].encode('ascii', errors='ignore').decode('CP1251')])

    return dict_parcer


result_list = list()
counter = 64
start = time.time()
while True:
    counter += 1
    url = f'https://cars.av.by/filter?brands[0][brand]=1216&brands[0][model]=5912&page={counter}'
    for_write = parce(url)
    list_for_sort = list(for_write.items())
    if list_for_sort == []:
        print(time.time() - start)
        break
    result_list.extend(list_for_sort)
result_list.sort(key=lambda i: i[1][1])

with open('parcer2_inf.csv', 'w', encoding='UTF-8', newline='\n') as file:
    writer_file = csv.writer(file, delimiter=':')
    writer_file.writerow(['ссылка', ['цена(byn)', 'цена(usd)', 'год выпуска', 'объем', 'тип двигателя', 'пробег']])
    for row in result_list:
        writer_file.writerow(row)

with open('parcer1_inf.json', 'w', newline='\n') as file:
    json.dump(result_list, file, indent=2, ensure_ascii=False)

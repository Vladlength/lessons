import json
import csv
from pprint import pprint

with open('parcer1_inf.json') as file:
    a = json.load(file)
    for i in a:
        print(*i)

# with open('parcer2_inf.csv', encoding='UTF-8') as file:
#     a = csv.reader(file)
#     for i in a:
#         print(*i)

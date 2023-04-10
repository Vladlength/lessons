import sys

# 1
num1 = int(input('Введите число: '))
num2 = int(input('Введите число: '))
try:
    res = num1 / num2
except ZeroDivisionError:
    print('На 0 делить нельзя')
else:
    res **= 2
    print(res)
finally:
    print('Программа закончена')

# 2
num1 = int(input('Введите число: '))
num2 = int(input('Введите число: '))
try:
    res = num1 / num2
except ZeroDivisionError:
    print('На 0 делить нельзя')
except ValueError:
    print('Проблема с типами данных')
except:
    print('Что-то не так')

# 3
while True:
    try:
        sub = input("Введите два числа: ").split(' ')
        sub = [int(i) for i in sub ]
    except ValueError:
        print("ValueError")
        sys.exit()
    else:
        try:
            res = sub[0] / sub[1]
        except ZeroDivisionError:
            print('На 0 делить нельзя')
        else:
            print(res)
            break

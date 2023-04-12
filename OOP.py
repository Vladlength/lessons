from faker import Faker
from random import randint
import csv


# 1
class Example:
    num1 = 2
    num2 = 5

    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def summary(self):
        return Example.num1 + Example.num2

    def degree(self, x, y):
        return x ** y


obj1 = Example(4, 2)
print(obj1.summary())
print(obj1.degree(3, 2))

# 2
class Calculator:
    def __init__(self):
        self.num1 = int(input('Введите число 1: '))
        self.num2 = int(input('Введите число 2: '))

    def plus(self):
        return self.num1 + self.num2

    def minus(self):
        return self.num1 - self.num2

    def multi(self):
        return self.num1 * self.num2

    def degree(self):
        return self.num1 ** self.num2

    def division(self):
        return self.num1 / self.num2

    def int_div(self):
        return self.num1 // self.num2


obg = Calculator()
print(obg.multi())
print(obg.minus())
print(obg.int_div())

# 3
class Example:

    def __init__(self, obg):
        self.len_obg = len(str(obg))
        self.obg = obg

    def method_1(self):
        conson = []
        vow = []
        if isinstance(self.obg, str):
            for i in self.obg:
                if i in 'йеуыаоэяию':
                    vow.append(i)
                elif i == ' ':
                    pass
                else:
                    conson.append(i)
            if len(vow) * len(conson) <= self.len_obg:
                return vow
            else:
                return conson
        if isinstance(self.obg, int):
            return self.len_obg * sum([int(i) for i in str(self.obg) if int(i) % 2 == 0])


f = Example('дядя вася')
h = Example(432)
print(f.method_1())
print(h.method_1())

# 4
class For_CSV:
    def Csv(self, name, old_salary, new_salary):
        self.name = name
        self.old = old_salary
        self.new = new_salary
        with open(f'{self.name}.csv', 'a', encoding="UTF-8") as file:
            fileWriter = csv.writer(file, delimiter=':')
            fileWriter.writerow([self.name, self.old, self.new])


class Employee:
    change = For_CSV()

    def __init__(self, name, surname, position, salary):
        self.name = name
        self.surname = surname
        self.position = position
        self.salary = salary

    def Name(self, mode='r', new_name=None):
        if mode == 'r':
            return self.name
        elif mode == 'w':
            self.name = new_name
            return self.name

    def Surname(self, mode='r', new_surname=None):
        if mode == 'r':
            return self.surname
        elif mode == 'w':
            self.surname = new_surname
            return self.surname

    def Position(self, mode='r', new_position=None):
        if mode == 'r':
            return self.position
        elif mode == 'w':
            self.position = new_position
            return self.position

    def Salary(self, mode='r', new_salary=None):
        if mode == 'r':
            return self.salary
        elif mode == 'w':
            self.change.Csv(self.name, self.salary, new_salary)
            self.salary = new_salary
            return self.salary

    def Salary_increaase(self, incre_percent=1):
        old = self.salary
        self.salary *= 1 + incre_percent / 100
        self.salary = int(self.salary)
        self.change.Csv(self.name, old, self.salary)
        return self.salary

    def Comparison(self, worker2):
        if self.salary > worker2.salary:
            return f'{self.salary} > {worker2.salary}'
        elif self.salary < worker2.salary:
            return f'{self.salary} < {worker2.salary}'
        else:
            return f'{self.salary} = {worker2.salary}'

    def inf(self):
        return [self.name, self.surname, self.position, self.salary]


fake = Faker('RU_ru')

list_workers = [Employee(fake.first_name(), fake.last_name(), fake.job(), round(randint(500, 2500), -2)) for i in
                range(3)]

print('inf:', list_workers[0].inf())
print('name:', list_workers[1].Name())
print('surname:', list_workers[2].Surname())
print('salary:', list_workers[1].Salary())
print(list_workers[1].inf())
list_workers[1].Salary('w', 1300)
list_workers[1].Position('w', 'Уборщик')
print(list_workers[1].inf())
list_workers[1].Salary_increaase(50)
print(list_workers[1].inf())
print(list_workers[1].Comparison(list_workers[0]))

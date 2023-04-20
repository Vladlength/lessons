import string


class House:

    def __init__(self, price=None, area=None):
        self._area = area
        self._price = price

    def final_price(self, discount):
        self.res = self._price - self._price * discount / 100
        return self.res


class Human:
    default_name = 'Ivan'
    default_age = 18

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None

    def info(self):
        print(self.name, self.age, self.__house, self.__money)

    @staticmethod
    def default_info():
        print(Human.default_name, Human.default_age)

    def earn_money(self, add_money):
        self.__money += add_money

    def __make_deal(self, house_obj, cost):
        self.__money -= cost
        self.__house = house_obj
        print('Покупка совершена успешно')

    def buy_house(self, house_obj, discount):
        final_cost = house_obj.final_price(discount)
        if self.__money >= final_cost:
            Human.__make_deal(self, house_obj, final_cost)
        else:
            print('Недостаточно средств')

    def house_get(self):
        return self.__house


class SmallHouse(House):

    def __init__(self):
        self.obj = 40 * 2


Human.default_info()
human_obj = Human()
human_obj.info()
human_obj.earn_money(100)
human_obj.info()
house_obj = House(100)
human_obj.buy_house(house_obj, 10)
human_obj.info()
small_house_obj = SmallHouse
# =============

class Alphabet:
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters

    def _print(self):
        print(self.letters)

    def letters_num(self):
        print(len(self.letters))


class EngAlphabet(Alphabet):
    __letters_num = 26

    def __init__(self):
        super().__init__('En', string.ascii_uppercase)

    def is_En_letter(self, letter):
        if letter.upper() in self.letters:
            print('Англ буква')
        else:
            print('не англ буква')

    def letters_num(self):
        return self.__letters_num

    @staticmethod
    def example():
        print('go home after dinner')


sad = EngAlphabet()
sad._print()
print(sad.letters_num())
sad.is_En_letter('F')
sad.is_En_letter('Щ')
sad.example()
#===========

class Tomato:
    states = ['росток', 'подходит', 'готов к употреблению']

    def __init__(self, index=0):
        self._index = index
        self._state = self.states[self._index]

    def grow(self):
        self._index += 1
        self._state = self.states[self._index]

    def is_ripe(self):
        return self._state == 'готов к употреблению'


class TomatoBush:
    def __init__(self, num):
        # список объектов класса томат
        self.tomatoes = [f'tomat{i}' for i in range(num)]
        for i in self.tomatoes:
            i = Tomato()

    def grow_all(self):
        for i in self.tomatoes:
            i.grow()

    def all_are_ripe(self):
        for i in self.tomatoes:
            if i == 'готов к употреблению':
                pass
            else:
                break
        return True

    def give_away_all(self):
        self.tomatoes = []


class Gardener:
    def __init__(self, name, plant: Tomato, plants=None):
        self.name = name
        self._plant = plant
        self.tomatoes = plants

    def work(self):
        #         садовник работает
        self._plant.grow()

    def harvest(self):
        try:
            if self.tomatoes.all_are_ripe():
                print('сбор урожая')
                self.tomatoes.give_away_all()
            else:
                print('еще не все созрели')
        except:
            if self._plant.is_ripe():
                print('сбор урожая')
                self._plant = None
            else:
                print('еще не все созрел')

    @staticmethod
    def knowledge_base():
        print(f'Меня зовут {name.name}, помидоры: {name.harvest()}')


tom = Tomato()
name = Gardener('ivan', tom)
name.knowledge_base()
TomBush = TomatoBush(5)
name.work()
name.harvest()
name.work()
name.harvest()

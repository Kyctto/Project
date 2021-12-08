# -*- coding: utf-8 -*-

from random import randint

# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет). +
# Кот живет с человеком в доме. +
# Для кота дом характеризируется - миской для еды и грязью. +
# Изначально в доме нет еды для кота и нет грязи. +

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.   +
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.  +
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.   +
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)  +

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.   +
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.

# -*- coding: utf-8 -*-

from random import randint


from termcolor import cprint

class Cat:

    def __init__(self, name):
        self.fullness = 50
        self.house = None
        self.name = name

    def __str__(self):
        return 'Я {}, моя сытость {}'.format(self.name, self.fullness)

    def eat(self):
        if self.house.cat_food >= 10:
            cprint('{} поел'.format(self.name), color='blue')
            self.fullness += 20
            self.house.cat_food -= 10
        else:
            cprint('{} голодает'.format(self.name), color='red')
            self.fullness -= 10


    def sleep(self):
        cprint('{} спит'.format(self.name), color='blue')
        self.fullness -= 10

    def fuck(self):
        cprint('{} бесоёбит'.format(self.name), color='blue')
        self.fullness -= 10
        self.house.pollution += 5

    def act(self):
        dice = randint(1, 2)
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        elif self.fullness <= 20:
            self.eat()
        elif dice == 1:
            self.fuck()
        else:
            self.sleep()


class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness)

    def eat(self):
        if self.house.food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 10
            self.house.food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 150
        self.fullness -= 10

    def watch_MTV(self):
        cprint('{} смотрел MTV целый день'.format(self.name), color='green')
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.food += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def take_a_cat(self, cat):
        cat.house = self.house
        cprint('{} подобрал кота {} и поселил его в дом'.format(self.name, cat.name), color='green')

    def buy_cat_food(self):
        if self.house.money >= 50:
            cprint('{} сходил коту за едой'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.cat_food += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def clean_house(self):
        if self.house.pollution >=100:
            cprint('{} убрался в доме'.format(self.name), color='magenta')
            self.house.pollution -= 100
            self.fullness -= 20

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} Вьехал в дом'.format(self.name), color='cyan')

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 3)
        if self.fullness < 30:
            self.eat()
        elif self.house.money < 70:
            self.work()
        elif self.house.food < 20:
            self.shopping()
        elif self.house.cat_food < 60:
            self.buy_cat_food()
        elif self.house.pollution > 100:
            self.clean_house()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.watch_MTV()


class House:

    def __init__(self):
        self.food = 50
        self.money = 0
        self.cat_food = 0
        self.pollution = 0
    def __str__(self):
        return 'В доме еды осталось {}, денег осталось {}, кашачей еды {}, грязно на {} процентов'.format(
            self.food, self.money, self.cat_food, self.pollution)


# citizens = [
#     Man(name='Бивис'),
#     Man(name='Батхед'),
#     Man(name='Кенни'),
# ]


my_sweet_home = House()
# for citisen in citizens:
#     citisen.go_to_the_house(house=my_sweet_home)
tihon = Cat(name='Тихон')
muhtar = Cat(name='Мухтар')
muhtar2 = Cat(name='Мухтар2')
muhtar3 = Cat(name='Мухтар3')
muhtar4 = Cat(name='Мухтар4')
muhtar5 = Cat(name='Мухтар5')

human = Man(name='Генаша')
human.go_to_the_house(house=my_sweet_home)
human.take_a_cat(cat=tihon)
human.take_a_cat(cat=muhtar)
human.take_a_cat(cat=muhtar2)
human.take_a_cat(cat=muhtar3)
human.take_a_cat(cat=muhtar4)
human.take_a_cat(cat=muhtar5)




for day in range(1, 366):
    print('================ день {} =================='.format(day))
    # for citisen in citizens:
    human.act()
    tihon.act()
    muhtar.act()
    muhtar2.act()
    muhtar3.act()
    muhtar4.act()
    # muhtar5.act()
    print('--- в конце дня ---')
    print(human)
    print(tihon)
    print(muhtar)
    print(muhtar2)
    print(muhtar3)
    print(muhtar4)
    # print(muhtar5)
    print(my_sweet_home)



# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)

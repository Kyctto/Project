# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint


######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.   +
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.    +
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,               +
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умрает от депресии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.


class House:

    def __init__(self):
        self.house_money = 100
        self.house_eat = 50
        self.house_enviroment = 0
        self.cat_food = 30

    def __str__(self):
        return 'В доме сейчас {} денег, {} еды, загрязнен на {} процентов, {} кошачей еды'.format(self.house_money,
                                                                                  self.house_eat, self.house_enviroment,
                                                                                  self.cat_food)

    def act(self):
        self.house_enviroment += 5


class Man():

    def __init__(self, name):
        self.name = name
        self.fullness = 30
        self.happyness = 100
        self.house = None

    def __str__(self):
        return '{}: сытоcть - {}, счастье - {}'.format(self.name, self.fullness, self.happyness)

    def go_to_the_house(self, house):
        self.house = house
        cprint('{} Вьехал в дом'.format(self.name), color='cyan')

    def eat(self):
        self.fullness += 30
        self.house.house_eat -= 30
        cprint('{} поел'.format(self.name), color='green')

    def act(self):
        if self.house.house_enviroment > 90:
            self.happyness -= 10
        if self.fullness <= 0:
            cprint('{} умер от голода'.format(self.name), color='red')
            return False
        if self.happyness < 10:
            cprint('{} умер от депрессии'.format(self.name), color='red')
            return False

        return True

    def pet_the_cat(self):
        self.fullness -= 10
        self.happyness += 5
        cprint('{} гладит кота'.format(self.name), color='blue')

class Husband(Man):

    def __str__(self):
        return 'Муж ' + super().__str__()

    def act(self):
        dice = randint(1, 6)
        if super().act():
            if self.fullness <= 30 and self.house.house_eat > 30:
                self.eat()
            elif self.happyness <= 50:
                if dice > 3:
                    self.gaming()
                else:
                    self.pet_the_cat()
            elif self.house.cat_food < 50:
                self.buy_catfood()
            elif self.house.house_money < 3000:
                self.work()
            else:
                if dice > 3:
                    self.gaming()
                else:
                    self.pet_the_cat()


    def work(self):
        self.fullness -= 10
        self.house.house_money += 150
        cprint('{} пошёл на работу'.format(self.name), color='blue')

    def gaming(self):
        self.fullness -= 10
        self.happyness += 20
        cprint('{} играет в WOT'.format(self.name), color='blue')

    def buy_catfood(self):
        self.fullness -= 10
        self.house.cat_food += 10
        self.house.house_money -= 10
        cprint('{} покупает еду коту'.format(self.name), color='blue')


class Wife(Man):

    def __str__(self):
        return 'Жена ' + super().__str__()

    def act(self):
        if super().act():
            if self.fullness <= 30 and self.house.house_eat > 30:
                self.eat()
            elif self.house.house_eat <= 60:
                self.shopping()
            elif self.happyness < 50:
                self.buy_fur_coat()
            elif self.house.house_enviroment > 50:
                self.clean_house()
            else:
                self.pet_the_cat()

    def shopping(self):
        self.fullness -= 10
        self.house.house_money -= 100
        self.house.house_eat += 100
        cprint('{} купила продукты'.format(self.name), color='blue')

    def buy_fur_coat(self):
        self.fullness -= 10
        self.house.house_money -= 350
        self.happyness += 60
        cprint('{} купила шубу'.format(self.name), color='blue')

    def clean_house(self):
        self.fullness -= 10
        if self.house.house_enviroment < 100:
            self.house.house_enviroment -= self.house.house_enviroment
        else:
            self.house.house_enviroment -= 100
        cprint('{} убралась дома'.format(self.name), color='blue')


# home = House()
# serge = Husband(name='Сережа')
# masha = Wife(name='Маша')
#
# serge.go_to_the_house(house=home)
# masha.go_to_the_house(house=home)
# for day in range(365):
#     cprint('================== День {} =================='.format(day), color='red')
#     home.act()
#     serge.act()
#     masha.act()
#     cprint(serge, color='cyan')
#     cprint(masha, color='cyan')
#     cprint(home, color='cyan')


######################################################## Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов


class Cat:

    def __init__(self, name, house):
        self.name = name
        self.fullness = 30
        self.house = house

    def __str__(self):
        return 'Кот {}, сытость - {}'.format(self.name, self.fullness)

    def act(self):
        if self.fullness < 1:
            return cprint('{} умер от голода'.format(self.name), color='red')
        dice = randint(1,6)
        if self.fullness < 40 and self.house.cat_food >= 10:
            self.eat()
        elif dice > 3:
            self.sleep()
        else: self.soil()

    def eat(self):
        self.fullness += 20
        self.house.cat_food -= 10
        cprint('Кот {} поел'.format(self.name), color='yellow')

    def sleep(self):
        self.fullness -= 10
        cprint('Кот {} спит'.format(self.name), color='yellow')

    def soil(self):
        self.fullness -= 10
        self.house.house_enviroment += 5
        cprint('Кот {} дерет обои'.format(self.name), color='yellow')

######################################################## Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)

class Child(Man):

    def __str__(self):
        return 'Ребенок' + super().__str__()

    def act(self):
        if self.fullness <= 0:
            return cprint('{} умер от голода'.format(self.name), color='red')
        elif self.fullness < 30:
            self.eat()
        else:
            self.sleep()

    def eat(self):
        self.fullness += 10
        self.house.house_eat -= 10
        cprint('{} поел'.format(self.name), color='white')

    def sleep(self):
        self.fullness -= 10
        cprint('{} поспал'.format(self.name), color='white')

######################################################## Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.


home = House()
serge = Husband(name='Сережа')
masha = Wife(name='Маша')
kolya = Child(name='Коля')
murzik = Cat(name='Мурзик', house=home)
serge.go_to_the_house(house=home)
masha.go_to_the_house(house=home)
kolya.go_to_the_house(house=home)

for day in range(365):
    cprint('================== День {} =================='.format(day), color='red')
    serge.act()
    masha.act()
    kolya.act()
    murzik.act()
    home.act()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(kolya, color='cyan')
    cprint(murzik, color='cyan')
    cprint(home, color='cyan')
#

# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')

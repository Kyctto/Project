# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())


class Water:

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Mud()


    def __str__(self):
        return 'Вода'


class Air:
    def __str__(self):
        return 'Воздух'

    def __add__(self, other):
        if isinstance(other, Fire):
            return Rain()
        elif isinstance(other, Earth):
            return Dust()


class Fire:
    def __str__(self):
        return 'Огонь'

    def __add__(self, other):
        if isinstance(other, Air):
            return Rain()
        elif isinstance(other, Earth):
            return Lava()


class Earth:
    def __str__(self):
        return 'Земля'

class Storm():
    def __str__(self):
        return 'Шторм'
class Mud():

    def __str__(self):
        return 'Грязь'

class Rain():

    def __str__(self):
        return 'Молния'

class Lava():

    def __str__(self):
        return 'Лава'

class Dust():

    def __str__(self):
        return 'Пыль'




print(Water(), '+', Earth(), '=', Water() + Earth())
print(Fire(), '+', Air(), '=', Fire() + Air())
print(Fire(), '+', Earth(), '=', Fire() + Earth())
# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.

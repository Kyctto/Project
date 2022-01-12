# -*- coding: utf-8 -*-

# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.
from random import randint

def one_day():
    dice = randint(1, 13)
    if dice == 5:
        dice = randint(1, 6)
        if dice == 1:
            raise IamGodError(day=day)
        if dice == 2:
            raise DrunkError(day=day)
        if dice == 3:
            raise CarCrashError(day=day)
        if dice == 4:
            raise GluttonyError(day=day)
        if dice == 5:
            raise DepressionError(day=day)
        if dice == 6:
            raise SuicideError(day=day)
    current_karma = randint(1, 7)
    return current_karma



class IamGodError(Exception):
    def __init__(self, day):
        self.day = day

    def __str__(self):
        return "Возомнил себя богом"

class DrunkError(Exception):
    def __init__(self, day):
        self.day = day

    def __str__(self):
        return "Нажрался как собака"

class CarCrashError(Exception):
    def __init__(self, day):
        self.day = day

    def __str__(self):
        return "Разбился на смерть"

class GluttonyError(Exception):
    def __init__(self, day):
        self.day = day

    def __str__(self):
        return "Обкушался"

class DepressionError(Exception):
    def __init__(self, day):
        self.day = day

    def __str__(self):
        return "Впал в депрессию"


class SuicideError(Exception):
    def __init__(self, day):
        self.day = day

    def __str__(self):
        return "Самоубился"



ENLIGHTENMENT_CARMA_LEVEL = 777
day = 1
karma = 0
exept_value = 0
while ENLIGHTENMENT_CARMA_LEVEL > karma:
    try:
        karma += one_day()
    except Exception as exp:
        print (f"Поймали ошибку {exp}, произошло в {exp.day} день")
        exept_value +=1

    finally:
        day += 1
print(f"Всё закончилось на {day} день, карма стала {karma}. Всего ошибок {exept_value}")

# https://goo.gl/JnsDqu

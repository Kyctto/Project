# -*- coding: utf-8 -*-
from random import randint

import simple_draw as sd


# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:

    def __init__(self):
        self.snowflake_x = randint(100, 600)
        self.snowflake_y = randint(500, 600)
        self.snowflake_length = randint(10, 50)

    def __str__(self):
        return ('flake')


    def clear_previous_picture(self):
        sd.start_drawing()
        point = sd.get_point(self.snowflake_x, self.snowflake_y)
        sd.snowflake(center=point, length=self.snowflake_length, color=sd.background_color)
        sd.finish_drawing()

    def move(self):
        self.snowflake_x += randint(-5, 20)
        self.snowflake_y -= 50

    def draw(self):
        sd.start_drawing()
        point = sd.get_point(self.snowflake_x, self.snowflake_y)
        sd.snowflake(center=point, length=self.snowflake_length, color=sd.COLOR_WHITE)
        sd.finish_drawing()

    def can_fall(self):
        if self.snowflake_y >= 5:
            return True

# Одна снежинка

# flake = Snowflake()
#
# while True:
#     flake.clear_previous_picture()
#     flake.move()
#     flake.draw()
#     if not flake.can_fall():
#         break
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break
i = 0
flakes = []
while i < 30:
    flake = Snowflake()
    flakes.append(flake)
    i += 1

def get_fallen_flakes():
    fallen_flakes = []
    for flake in flakes:
        if not flake.can_fall():
            fallen_flakes.append(flake)
    return fallen_flakes


# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
# flakes = get_flakes(count=N)  # создать список снежинок

while True:
    for flake in flakes:
        flake.clear_previous_picture()
        flake.move()
        flake.draw()
    fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
    if fallen_flakes:
        for flake in fallen_flakes:
            flakes.remove(flake)
            flake = Snowflake()
            flakes.append(flake)
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()

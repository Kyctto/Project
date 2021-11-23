# -*- coding: utf-8 -*-

import simple_draw as sd

# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
#
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall

from snowfall import create_snowflake
from snowfall import move_snowflake
from snowfall import paint_snowflake
from snowfall import number_of_end_snowflake
from snowfall import deleting_snowflake

create_snowflake(30)
while True:

    paint_snowflake(color=sd.background_color)

    move_snowflake()

    paint_snowflake(color=sd.COLOR_WHITE)

    if number_of_end_snowflake():
        x = len(number_of_end_snowflake())
        print('Есть')
        deleting_snowflake(number_of_end_snowflake())
        create_snowflake(x)
    #       создать_снежинки(count)  найти вхождения значений списка удалённых в список Н
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()

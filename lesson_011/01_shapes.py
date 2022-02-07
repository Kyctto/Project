# -*- coding: utf-8 -*-

import simple_draw as sd

# На основе вашего кода из решения lesson_004/01_shapes.py сделать функцию-фабрику,
# которая возвращает функции рисования треугольника, четырехугольника, пятиугольника и т.д.
#
# Функция рисования должна принимать параметры
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Функция-фабрика должна принимать параметр n - количество сторон.


def get_polygon(n):

    def draw_triangle(point, angle, length):
        angle_changer = 360 / n
        for i in range(n):
            new_angle = angle_changer * i
            vector = sd.get_vector(start_point=point, angle=angle + new_angle, length=length)
            point = vector.end_point
            vector.draw()

    return draw_triangle


draw_triangle = get_polygon(n=8)
draw_triangle(point=sd.get_point(200, 200), angle=13, length=100)

sd.pause()

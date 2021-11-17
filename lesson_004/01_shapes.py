# -*- coding: utf-8 -*-

import simple_draw as sd

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg


#
# def sqare (start_point,start_angle,length):
#     v1 = sd.get_vector(start_point=start_point,angle=start_angle,length=length,width=3)
#     v1.draw()
#     v2 = sd.get_vector(start_point=v1.end_point,angle=start_angle+90,length=length,width=3)
#     v2.draw()
#     v3 = sd.get_vector(start_point=v2.end_point, angle=start_angle + 90 + 90, length=length, width=3)
#     v3.draw()
#     v4 = sd.get_vector(start_point=v3.end_point, angle=start_angle + 90 + 90 + 90, length=length, width=3)
#     v4.draw()
#
# def five_angle (start_point,start_angle,length):
#     v1 = sd.get_vector(start_point=start_point,angle=start_angle,length=length,width=3)
#     v1.draw()
#     v2 = sd.get_vector(start_point=v1.end_point,angle=start_angle+72,length=length,width=3)
#     v2.draw()
#     v3 = sd.get_vector(start_point=v2.end_point, angle=start_angle + 72 + 72, length=length, width=3)
#     v3.draw()
#     v4 = sd.get_vector(start_point=v3.end_point, angle=start_angle + 72 + 72 + 72, length=length, width=3)
#     v4.draw()
#     v5 = sd.get_vector(start_point=v4.end_point, angle=start_angle + 72 + 72 + 72 + 72, length=length, width=3)
#     v5.draw()
#
# def six_angle (start_point,start_angle,length):
#     v1 = sd.get_vector(start_point=start_point,angle=start_angle,length=length,width=3)
#     v1.draw()
#     v2 = sd.get_vector(start_point=v1.end_point,angle=start_angle+60,length=length,width=3)
#     v2.draw()
#     v3 = sd.get_vector(start_point=v2.end_point, angle=start_angle + 60 + 60, length=length, width=3)
#     v3.draw()
#     v4 = sd.get_vector(start_point=v3.end_point, angle=start_angle + 60 + 60 + 60, length=length, width=3)
#     v4.draw()
#     v5 = sd.get_vector(start_point=v4.end_point, angle=start_angle + 60 + 60 + 60 + 60, length=length, width=3)
#     v5.draw()
#     v6 = sd.get_vector(start_point=v5.end_point, angle=start_angle + 60 + 60 + 60 + 60 + 60, length=length, width=3)
#     v6.draw()

# six_angle(x,0,100)

def draw_figure (start_point, side_value, angle, length, width):
    angle_changer = 360/side_value
    for i in range (side_value):
        new_angle = angle_changer * i
        vector = sd.get_vector(start_point=start_point, angle=angle + new_angle, length=length, width=width)
        start_point = vector.end_point
        vector.draw()



draw_vector(start_point=x, side_value=36, angle=0, length=15, width=2)


def triangle (start_point,start_angle,length):
    side_value = 3
    draw_vector(start_point=start_point, side_value=side_value, angle=start_angle, length=length, width=2)
# triangle(x,0, 100)



# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()

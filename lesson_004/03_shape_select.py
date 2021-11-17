# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

x = sd.get_point(300,300)
def draw_figure (start_point, side_value, angle, length, width, color):
    angle_changer = 360/side_value
    for i in range (side_value):
        new_angle = angle_changer * i
        vector = sd.get_vector(start_point=start_point, angle=angle + new_angle, length=length, width=width)
        start_point = vector.end_point
        vector.draw(color=color)
print('Введите колличество граней фигуры от 3 до 7')
sides = int(input())
draw_figure(start_point=x,side_value=sides,angle=0,length=70,width=2,color=sd.COLOR_CYAN)
sd.pause()

# -*- coding: utf-8 -*-
import simple_draw as sd

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

x = sd.get_point(300,300)
def draw_figure (start_point, side_value, angle, length, width, color):
    angle_changer = 360/side_value
    for i in range (side_value):
        new_angle = angle_changer * i
        vector = sd.get_vector(start_point=start_point, angle=angle + new_angle, length=length, width=width)
        start_point = vector.end_point
        vector.draw(color=color)
print('Введите номер требуемого цвета  1 - Красный, 2 - Зеленый,3 - Синий,4 - Желный')

color_value = 0
color_value = int(input())


if color_value == 1:
    color = sd.COLOR_RED,
elif color_value == 2:
    color = sd.COLOR_GREEN
elif color_value == 3:
    color = sd.COLOR_BLUE
elif color_value == 4:
    color = sd.COLOR_YELLOW
else: print('Вы ввели не верное значение')
angle = 0
for i in range (3,7):
    draw_figure(start_point=x,side_value=i,angle=angle,length=70,width=2,color=color)
    x=sd.random_point()
    angle = sd.random_number(0, 359)



sd.pause()

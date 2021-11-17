# -*- coding: utf-8 -*-

import simple_draw as sd

# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения
x = sd.get_point(300, 300)


def draw_branches(start_point, angle, length):
    if length < 10:
        return
    v1 = sd.get_vector(start_point=start_point, angle=angle + 30, length=length)
    v1.draw()
    next_point1 = v1.end_point
    next_angle1 = angle + 30
    next_length1 = length * 0.75
    v2 = sd.get_vector(start_point=start_point, angle=angle - 30, length=length)
    v2.draw()
    next_point2 = v2.end_point
    next_angle2 = angle - 30
    next_length2 = length * 0.75
    draw_branches(start_point=next_point1, angle=next_angle1, length=next_length1)
    draw_branches(start_point=next_point2, angle=next_angle2, length=next_length2)


# root_point = sd.get_point(300, 30)
# draw_branches(start_point=root_point, angle=90, length=100)
# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()
def draw_random_branches(start_point, angle, length):
    if length < 4:
        return
    v1 = sd.get_vector(start_point=start_point, angle=angle + sd.random_number(18, 42), length=length)
    v1.draw()
    next_point1 = v1.end_point
    next_angle1 = angle + sd.random_number(18, 42)
    next_length1 = length * sd.random_number(60, 90) / 100
    v2 = sd.get_vector(start_point=start_point, angle=angle - sd.random_number(18, 42), length=length)
    v2.draw()
    next_point2 = v2.end_point
    next_angle2 = angle - sd.random_number(18, 42)
    next_length2 = length * sd.random_number(60, 90) / 100
    draw_random_branches(start_point=next_point1, angle=next_angle1, length=next_length1)
    draw_random_branches(start_point=next_point2, angle=next_angle2, length=next_length2)


root_point = sd.get_point(300, 30)
draw_random_branches(start_point=root_point, angle=90, length=70)
sd.pause()

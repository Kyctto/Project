# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)
# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

snowflake_value = 5
# Высота всегда одна и таже

snowflake_listX = []
length_list = []
# Задаем список параметров по горизонтали
for i in range (snowflake_value):
    snowflake_listX.append(sd.random_number(0,400))
    length_list.append(sd.random_number(10,50))
print(snowflake_listX)
snowflake_listY = []
for i in range (snowflake_value):
    snowflake_listY.append(600)
# print(snowflake_listY)
# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()

while True:

    sd.start_drawing()
    for i in range (snowflake_value):

        point = sd.get_point(snowflake_listX[i], snowflake_listY[i])
        sd.snowflake(center=point, length=length_list[i], color=sd.background_color)
        snowflake_listX[i] += 10
        snowflake_listY[i] -= 50
        point2 = sd.get_point(snowflake_listX[i], snowflake_listY[i],)
        sd.snowflake(center=point2, length=length_list[i], color=sd.COLOR_WHITE)
        if snowflake_listY[i] < 50:
            break

    sd.finish_drawing()
    sd.sleep(0.1)
    if snowflake_listY[i] < -50:
        break


    if sd.user_want_exit():
        break

sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg



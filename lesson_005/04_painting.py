# -*- coding: utf-8 -*-

# Создать пакет, в который скопировать функции отрисовки из предыдущего урока
#  - радуги +
#  - стены +
#  - дерева +
#  - смайлика +
#  - снежинок +
# Функции по модулям разместить по тематике. Название пакета и модулей - по смыслу.
# Создать модуль с функцией отрисовки кирпичного дома с широким окном и крышей.

# С помощью созданного пакета нарисовать эпохальное полотно "Утро в деревне".
# На картине должны быть:
#  - кирпичный дом, в окошке - смайлик.
#  - слева от дома - сугроб (предположим что это ранняя весна)
#  - справа от дома - дерево (можно несколько)
#  - справа в небе - радуга, слева - солнце (весна же!)
# пример см. lesson_005/results/04_painting.jpg
# Приправить своей фантазией по вкусу (коты? коровы? люди? трактор? что придумается)

from Painting.House import house
from Painting.other import smile
from Painting.nature import rainbow
from Painting.nature import tree
from Painting.nature import snowfall
import simple_draw as sd
sd.resolution = (1800,800)
sd.background_color = (15,15,140)

house(left_cornerX=600, left_cornerY=100)
smile(coordinateX=800, coordinateY=235, color=sd.COLOR_YELLOW)

tree_point = sd.get_point(1200, 100)
tree(start_point=tree_point, length=50)
snowfall(snowflake_value=10)
rainbow(radius=900, start_point_x=900)

def sun(coordinateX=100, coordinateY=100):
    centr = sd.get_point(coordinateX,coordinateY)
    sd.circle(center_position=centr, radius=50, width=0)
    for angle in range(0,361,30):
        sd.vector(start=centr, angle=angle, length=100, width=2)

sun(1600,650)

sd.pause()



# Усложненное задание (делать по желанию)
# Анимировать картину.
# Пусть слева идет снегопад, радуга переливается цветами, смайлик моргает, солнце крутит лучами, етс.
# Задержку в анимировании все равно надо ставить, пусть даже 0.01 сек - так библиотека устойчивей работает.

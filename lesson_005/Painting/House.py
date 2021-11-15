import simple_draw


def house(left_cornerX= 50,left_cornerY= 70) -> object:
    import simple_draw as sd

    # параметры дома и кирпича
    house_length = 400
    house_higth = 250
    brick_length = 50
    brick_higth = 30
    right_cornerX = left_cornerX + house_length
    right_cornerY = left_cornerY + house_higth
    # Вводим переменные для циклов
    start_pointX1 = left_cornerX
    start_pointY1 = left_cornerY

    # Рисуем горизонтальные линии
    while True:
        left_corner1 = sd.get_point(start_pointX1, start_pointY1)
        sd.vector(start=left_corner1, angle= 0,length= house_length, color=sd.COLOR_WHITE)
        start_pointY1 += brick_higth
        if start_pointY1 > house_higth + 1 + left_cornerY:
            break

    # Рисуем вертикальные линии
    start_pointY1 = left_cornerY - brick_higth
    while True:
        start_pointX1 = left_cornerX
        start_pointY1 += brick_higth
        if start_pointY1 > house_higth - 29 + left_cornerY:
            break
        while start_pointX1 < house_length + left_cornerX:
            left_corner = sd.get_point(start_pointX1, start_pointY1)
            sd.vector(start=left_corner, angle=90, length=brick_higth, color=sd.COLOR_WHITE)
            start_pointX1 += brick_length
        start_pointX1 = left_cornerX + brick_length/2
        start_pointY1 += brick_higth
        if start_pointY1 > house_higth -29 + left_cornerY:
            break
        while start_pointX1 < house_length + left_cornerX:
            left_corner = sd.get_point(start_pointX1, start_pointY1)
            sd.vector(start=left_corner, angle=90, length= brick_higth, color=sd.COLOR_WHITE)
            start_pointX1 += brick_length

    # Рисуем левую и правую стену
    left_corner = sd.get_point(left_cornerX, left_cornerY)
    sd.vector(left_corner, angle= 90, length=house_higth, color= sd.COLOR_RED)
    right_corner = sd.get_point(left_cornerX + house_length, left_cornerY)
    sd.vector(right_corner, angle= 90, length= house_higth, color= sd.COLOR_RED)

    # Рисуем крышу
    x1=sd.get_point(left_cornerX-30, right_cornerY)
    x2=sd.get_point(right_cornerX +30,right_cornerY)
    x3=sd.get_point(left_cornerX + house_length/2, left_cornerY + house_higth + 60)
    point_list = [x1, x2, x3]
    sd.polygon(point_list=point_list,width=0, color=sd.COLOR_DARK_RED)

    # Рисуем окно
    left_bottom = sd.get_point(left_cornerX + house_length/3,left_cornerY + house_higth/3)
    right_top = sd.get_point(left_cornerX + house_length/3 + 150, left_cornerY + house_higth/3 + 100)
    sd.rectangle(left_bottom=left_bottom, right_top=right_top, width=0, color=sd.background_color)

    # рисуем рамку
    left_bottom = sd.get_point(left_cornerX + house_length/3 -1,left_cornerY + house_higth/3 -1)
    right_top = sd.get_point(left_cornerX + house_length/3 + 151, left_cornerY + house_higth/3 + 101)
    sd.rectangle(left_bottom=left_bottom, right_top=right_top, width=1, color=sd.COLOR_DARK_YELLOW)

if __name__ == "__main__":
    house()
    simple_draw.pause()
import simple_draw
simple_draw.resolution = (900,600)

def house(left_cornerX= 1,left_cornerY= 100):
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

    # TODO Рисуем крышу, надо отрисовать треугольник по списку точек

    sd.polygon()


house()
simple_draw.pause()

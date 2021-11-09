import simple_draw as sd

def smile(coordinateX, coordinateY, color):
    point = sd.get_point(coordinateX, coordinateY)
    # Рисуем круг
    sd.circle(center_position=point, color=color)
    # Создаем рот
    point1 = sd.get_point(coordinateX - 20, coordinateY - 10)
    point2 = sd.get_point(coordinateX, coordinateY - 20)
    point3 = sd.get_point(coordinateX + 20, coordinateY - 10)
    point_list = [point1, point2, point3]
    sd.lines(point_list=point_list,color=color)
    # Рисуем глаза
    left_eye = sd.get_point(coordinateX - 20, coordinateY + 20)
    right_eye = sd.get_point(coordinateX + 20, coordinateY + 20)
    sd.circle(center_position=left_eye,radius=5,color=color)
    sd.circle(center_position=right_eye,radius=5,color=color)



def wall():
    x_start_left = -110
    x_right_corner = x_start_left + 100
    y_start_left = 1
    y_right_corner = y_start_left + 50
    for _ in range(13):
        for _ in range(13):
            left_corner = sd.get_point(x_start_left, y_start_left)
            right_corner = sd.get_point(x_right_corner, y_right_corner)
            sd.rectangle(left_bottom=left_corner, right_top=right_corner, width=1)
            x_start_left += 100
            x_right_corner += 100
        x_start_left -= 1350
        x_right_corner = x_start_left + 100
        y_start_left += 50
        y_right_corner = y_start_left + 50

wall()
sd.pause()
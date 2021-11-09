import simple_draw as sd



def rainbow(radius= 400, start_point_x= 300 , start_point_y= -200):

    rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                      sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
    point = sd.get_point(start_point_x,start_point_y)
    radius = radius
    step = 10
    for color in rainbow_colors:
        sd.circle(center_position=point, radius=radius,color=color, width=10)
        radius += step
    sd.pause()




def tree (start_point, angle, length):

    if length < 4:
        return
    v1 = sd.get_vector(start_point=start_point, angle=angle + sd.random_number(18, 42), length=length)
    v1.draw(color=sd.COLOR_GREEN)
    next_point1 = v1.end_point
    next_angle1 = angle + sd.random_number(18, 42)
    next_length1 = length * sd.random_number(60, 90) / 100
    v2 = sd.get_vector(start_point=start_point, angle=angle - sd.random_number(18, 42), length=length)
    v2.draw(color=sd.COLOR_GREEN)
    next_point2 = v2.end_point
    next_angle2 = angle - sd.random_number(18, 42)
    next_length2 = length * sd.random_number(60, 90) / 100
    tree(start_point=next_point1, angle=next_angle1, length=next_length1)
    tree(start_point=next_point2, angle=next_angle2, length=next_length2)
# root_point = sd.get_point(300, 30)
# tree(start_point=root_point,angle=90, length=70)
# rainbow()
# sd.pause()

def snowfall(snowflake_value= 5):

    snowflake_listX = []
    length_list = []
    for i in range(snowflake_value):
        snowflake_listX.append(sd.random_number(0, 400))
        length_list.append(sd.random_number(10, 50))
    snowflake_listY = []
    for i in range(snowflake_value):
        snowflake_listY.append(600)

    while True:

        sd.start_drawing()
        for i in range(snowflake_value):

            point = sd.get_point(snowflake_listX[i], snowflake_listY[i])
            sd.snowflake(center=point, length=length_list[i], color=sd.background_color)
            snowflake_listX[i] += 10
            snowflake_listY[i] -= 50
            point2 = sd.get_point(snowflake_listX[i], snowflake_listY[i], )
            sd.snowflake(center=point2, length=length_list[i], color=sd.COLOR_WHITE)
            if snowflake_listY[i] < 50:
                break

        sd.finish_drawing()
        sd.sleep(0.1)
        if snowflake_listY[i] < -50:
            break

        if sd.user_want_exit():
            break
snowfall()
sd.pause()
# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка

snowflake_list_x = []
snowflake_list_y = []
length_list = []
import simple_draw as sd
sd.resolution = (1000,700)
def create_snowflake(x=5):
    # Задаем список параметров (Координаты и длинна снежинки)
    global snowflake_value
    snowflake_value = x

    for i in range(snowflake_value):
        snowflake_list_x.append(sd.random_number(0, 800))
        length_list.append(sd.random_number(10, 50))
        snowflake_list_y.append(sd.random_number(550, 750))
    print(snowflake_list_x)
#
def paint_snowflake(color=sd.background_color):
    sd.start_drawing()
    for i in range(len(snowflake_list_x)):
        point = sd.get_point(snowflake_list_x[i], snowflake_list_y[i])
        sd.snowflake(center=point, length=length_list[i], color=color)
    sd.finish_drawing()
#
def move_snowflake():
    for i in range (len(snowflake_list_x)):
        snowflake_list_x[i] += 10
        snowflake_list_y[i] -= 50
#
def number_of_end_snowflake():
    numbers=[]
    for i in range(len(snowflake_list_x)):
        if snowflake_list_y[i] < 50:
            numbers.append(i)

    return numbers
#
def deleting_snowflake(numbers):
    for i in reversed(numbers):
        snowflake_list_x.pop(i)
        snowflake_list_y.pop(i)
        length_list.pop(i)






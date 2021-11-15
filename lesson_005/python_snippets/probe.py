import simple_draw


def sun(coordinateX=100, coordinateY=100):
    import simple_draw as sd
    centr = sd.get_point(coordinateX,coordinateY)
    sd.circle(center_position=centr, radius=50, width=0)
    for angle in range(0,361,30):
        sd.vector(start=centr, angle=angle, length=100, width=2)


sun()
simple_draw.pause()
from cs1media import *

black = (0, 0, 0)

def draw_line(canvas, p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    for i in range(100):
        t = i / 99
        x = x1 + (x2 - x1) * t
        y = y1 + (y2 - y1) * t
        canvas.set(x, y, black)


def draw_rectangle(canvas, width, height, center):
    pass


canvas = create_picture(200, 200, 'white')

draw_line(canvas, (20, 100), (10, 10))
draw_line(canvas, (50, 50), (50, 80))
draw_line(canvas, (20, 50), (50, 50))
draw_rectangle(canvas, 60, 20, (100, 100))

canvas.show()

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
    xc, yc = center
    p1 = (round(xc - width / 2), round(yc - height / 2))
    p2 = (round(xc - width / 2), round(yc + height / 2))
    p3 = (round(xc + width / 2), round(yc + height / 2))
    p4 = (round(xc + width / 2), round(yc - height / 2))

    draw_line(canvas, p1, p2)
    draw_line(canvas, p2, p3)
    draw_line(canvas, p3, p4)
    draw_line(canvas, p4, p1)


def draw_square(canvas, side, center):
    draw_rectangle(canvas, side, side, center)


canvas = create_picture(200, 200, 'white')

draw_line(canvas, (20, 100), (10, 10))
draw_line(canvas, (50, 50), (50, 80))
draw_line(canvas, (20, 50), (50, 50))
draw_rectangle(canvas, 60, 20, (100, 100))
draw_square(canvas, 30, (150, 150))

canvas.show()

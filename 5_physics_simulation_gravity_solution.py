from cs1graphics import *
from time import sleep

(gx, gy) = (0, 9.8) # m/s^2
meters_per_pixel = 0.01 # m/pixel
canvas_size = 1000 # pixels (= 10 m)


def create_ball(canvas, radius, position, velocity):
    (x, y) = position
    shape = Circle(radius, Point(x/meters_per_pixel, y/meters_per_pixel))
    shape.setFillColor('black')
    canvas.add(shape)
    canvas.refresh()
    return (shape, position, velocity)


def update(canvas, balls, delta_t):
    for i in range(len(balls)):
        (shape, (x, y), (vx, vy)) = balls[i]

        vx += gx * delta_t
        vy += gy * delta_t

        x += vx * delta_t
        y += vy * delta_t

        shape.moveTo(x/meters_per_pixel, y/meters_per_pixel)

        balls[i] = (shape, (x, y), (vx, vy))

    sleep(delta_t)
    canvas.refresh()


my_canvas = Canvas(canvas_size, canvas_size)
my_canvas.setAutoRefresh(False)

ball1 = create_ball(my_canvas, 30, (1, 1), (0, 0))
ball2 = create_ball(my_canvas, 50, (2, 1), (5, 0))
ball3 = create_ball(my_canvas, 10, (1, 9), (5, -5))

my_balls = [ball1, ball2, ball3]

simulation_length = 10 # s
update_per_second = 60 # updates/s
for i in range(simulation_length * update_per_second):
    update(my_canvas, my_balls, 1/update_per_second)

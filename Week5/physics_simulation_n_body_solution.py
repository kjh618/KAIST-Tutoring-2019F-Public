from cs1graphics import *
from time import sleep
from math import atan2, cos, sin

grav_constant = 6.674e-11 # m^3 kg^-1 s^-2
meters_per_pixel = 3e8 # m/pixel
canvas_size = 1000 # pixels (= 3e11 m)


def create_body(canvas, radius, color, mass, position, velocity):
    (x, y) = position

    shape = Circle(radius, Point(x/meters_per_pixel, y/meters_per_pixel))
    shape.setBorderWidth(0)
    shape.setFillColor(color)

    canvas.add(shape)
    canvas.refresh()

    return (shape, mass, position, velocity)


def distance_sq(p1, p2):
    (x1, y1) = p1
    (x2, y2) = p2
    return (x2 - x1) ** 2 + (y2 - y1) ** 2


def update(canvas, bodies, delta_t, update_interval):
    accelerations = []
    for cur in bodies:
        (_, _, (x_cur, y_cur), _) = cur
        (ax, ay) = (0, 0)
        for other in bodies:
            if other is cur:
                continue
            (_, m_other, (x_other, y_other), _) = other
            a = grav_constant * m_other / distance_sq((x_cur, y_cur), (x_other, y_other))
            theta = atan2(y_other - y_cur, x_other - x_cur)
            ax += a * cos(theta)
            ay += a * sin(theta)
        accelerations.append((ax, ay))

    for i in range(len(bodies)):
        (shape, m, (x, y), (vx, vy)) = bodies[i]
        (ax, ay) = accelerations[i]

        vx += ax * delta_t
        vy += ay * delta_t

        x += vx * delta_t
        y += vy * delta_t

        shape.moveTo(x/meters_per_pixel, y/meters_per_pixel)

        bodies[i] = (shape, m, (x, y), (vx, vy))

    sleep(update_interval)
    canvas.refresh()


space = Canvas(canvas_size, canvas_size, 'black')
space.setAutoRefresh(False)

center = meters_per_pixel * canvas_size / 2
sun = create_body(space, 3, 'yellow', 1.989e30, (center, center), (0, 0))
mercury = create_body(space, 2, 'gray', 3.285e23, (center, center - 5.791e10), (4.736e4, 0))
venus = create_body(space, 2, 'orange', 4.867e24, (center, center - 1.082e11), (3.502e4, 0))
earth = create_body(space, 2, 'blue', 5.972e24, (center, center - 1.496e11), (2.978e4, 0))
moon = create_body(space, 1, 'gray', 7.348e22, (center, center - 1.496e11 - 3.844e8), (2.978e4 + 1.022e3, 0))

solar_system = [sun, mercury, venus, earth, moon]

seconds_per_day = 24*60*60 # s/day
update_per_second = 60 # updates/s
while True:
    update(space, solar_system, seconds_per_day/2, 1/update_per_second) # 1 s = 30 days

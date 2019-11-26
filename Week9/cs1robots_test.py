from cs1robots import *


def turn_right(robot):
    for _ in range(3):
        robot.turn_left()


create_world()

hubo = Robot()
hubo.set_pause(0.3)

for _ in range(3):
    hubo.move()
hubo.turn_left()
for _ in range(3):
    hubo.move()
turn_right(hubo)
for _ in range(3):
    hubo.move()

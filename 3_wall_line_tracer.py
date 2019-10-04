from cs1robots import *

load_world('my_worlds/3_wall_line_3.wld')

hubo = Robot()
hubo.set_trace('blue')


def turn_right():
    for i in range(3):
        hubo.turn_left()

def move_straight():
    while hubo.front_is_clear():
        hubo.move()

def turn():
    if not hubo.front_is_clear():
        if hubo.right_is_clear():
            turn_right()
        else:
            hubo.turn_left()

while not hubo.on_beeper():
    move_straight()
    turn()
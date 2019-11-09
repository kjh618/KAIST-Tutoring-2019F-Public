from cs1robots import *

load_world('my_worlds/wall_line_1.wld')

hubo = Robot()
hubo.set_trace('blue')


def hubo_turn_right():
    for i in range(3):
        hubo.turn_left()

def move_straight():
    while hubo.front_is_clear():
        hubo.move()


while not hubo.on_beeper():
    if hubo.left_is_clear():
        hubo.turn_left()
    elif hubo.right_is_clear():
        hubo_turn_right()
    move_straight()

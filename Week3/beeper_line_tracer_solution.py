from cs1robots import *

load_world('my_worlds/beeper_line_3.wld')

delay = 0

hubo = Robot(avenue=2, street=2)
hubo.set_trace('blue')
hubo.set_pause(delay)

lefty = Robot(avenue=2, street=3, color='light_blue')
lefty.set_trace('lightblue')
lefty.set_pause(delay)

righty = Robot(avenue=2, street=1, color='light_blue')
righty.set_trace('lightblue')
righty.set_pause(delay)


def turn_back(robot):
    robot.turn_left()
    robot.turn_left()

def turn_right(robot):
    for i in range(3):
        robot.turn_left()

def move_straight_together():
    hubo.move()
    lefty.move()
    righty.move()
    while not (lefty.on_beeper() or righty.on_beeper()):
        hubo.move()
        lefty.move()
        righty.move()

def turn_left_together():
    hubo.turn_left()

    turn_back(lefty)
    lefty.move()
    lefty.turn_left()
    lefty.move()
    turn_back(lefty)

    righty.move()
    righty.turn_left()
    righty.move()

def turn_right_together():
    turn_right(hubo)

    lefty.move()
    turn_right(lefty)
    lefty.move()

    turn_back(righty)
    righty.move()
    turn_right(righty)
    righty.move()
    turn_back(righty)


while not (lefty.on_beeper() and righty.on_beeper()):
    if lefty.on_beeper():
        turn_left_together()
    elif righty.on_beeper():
        turn_right_together()
    move_straight_together()

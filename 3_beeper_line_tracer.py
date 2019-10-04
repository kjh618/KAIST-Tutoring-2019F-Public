from cs1robots import *

load_world('my_worlds/3_beeper_line_2.wld')

delay = 0.5

hubo = Robot(avenue=2, street=2)
hubo.set_trace('blue')
hubo.set_pause(delay)

lefty = Robot(avenue=2, street=3, color='light_blue')
lefty.set_trace('lightblue')
lefty.set_pause(delay)

righty = Robot(avenue=2, street=1, color='light_blue')
righty.set_trace('lightblue')
righty.set_pause(delay)


def turn_right(robot):
    for i in range(3):
        robot.turn_left()

def turn_back(robot):
    robot.turn_left()
    robot.turn_left()

def move_straight():
    while not lefty.on_beeper() and not righty.on_beeper():
        hubo.move()
        lefty.move()
        righty.move()

def turn():
    if lefty.on_beeper() and righty.on_beeper():
        return

    elif lefty.on_beeper():
        turn_back(lefty)
        lefty.move()
        turn_right(lefty)

        hubo.turn_left()
        hubo.move()
        
        righty.move()
        righty.turn_left()
        righty.move()
        righty.move()
        
    elif righty.on_beeper():
        turn_back(righty)
        righty.move()
        righty.turn_left()
        
        turn_right(hubo)
        hubo.move()

        lefty.move()
        turn_right(lefty)
        lefty.move()
        lefty.move()

while not (lefty.on_beeper() and righty.on_beeper()):
    move_straight()
    turn()
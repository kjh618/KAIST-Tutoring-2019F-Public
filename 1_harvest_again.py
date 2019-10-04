from cs1robots import *

load_world('worlds/harvest2.wld')
hubo = Robot()
hubo.set_trace('blue')


def turn_right():
    for i in range(3):
        hubo.turn_left()

hubo.turn_left()
for i in range(6):
    hubo.move()

for i in range(5):
    if i <= 2:
        n = 1 + 4 * i

        for j in range(n):
            if j % 2 == 0:
                hubo.pick_beeper()
            hubo.move()
        turn_right()
        hubo.move()
        turn_right()
        for j in range(n):
            if j % 2 == 0:
                hubo.pick_beeper()
            hubo.move()

        hubo.move()
        hubo.pick_beeper()
        if i != 2:
            hubo.move()
            hubo.turn_left()
            hubo.move()
            hubo.turn_left()

    else:
        hubo.turn_left()
        hubo.move()
        hubo.turn_left()
        hubo.move()
        hubo.pick_beeper()
        hubo.move()

        n = 7 + 4 * (3 - i)

        for j in range(n):
            if j % 2 == 1:
                hubo.pick_beeper()
            hubo.move()
        hubo.pick_beeper()
        turn_right()
        hubo.move()
        turn_right()
        for j in range(n):
            if j % 2 == 1:
                hubo.pick_beeper()
            hubo.move()
        hubo.pick_beeper()

hubo.turn_left()
hubo.move()
hubo.turn_left()
hubo.move()
hubo.pick_beeper()

from cs1graphics import *
import time

world = None


class World:
    def __init__(self, avenues, streets):
        self.avenues = avenues
        self.streets = streets
        self.canvas = Canvas(50 * (avenues + 2), 50 * (streets + 2))


    def add(self, robot):
        self.canvas.add(robot.layer)


class Robot:
    def __init__(self, color='gray', orientation='E', avenue=1, street=1):
        if orientation == 'N':
            self.orientation = (0, -1)
        elif orientation == 'W':
            self.orientation = (-1, 0)
        elif orientation == 'E':
            self.orientation = (1, 0)
        elif orientation == 'S':
            self.orientation = (0, 1)

        self.layer = Layer()
        self.layer.moveTo(50 * avenue, 50 * (world.streets + 2 - street))

        self.body = Square(30)
        self.body.setFillColor(color)
        self.layer.add(self.body)

        self.dot = Circle(3)
        self.dot.moveTo(10 * self.orientation[0], 10 * self.orientation[1])
        self.dot.setFillColor('black')
        self.layer.add(self.dot)

        world.add(self)

        self.delay = 0


    def move(self):
        self.layer.move(50 * self.orientation[0], 50 * self.orientation[1])

        time.sleep(self.delay)


    def turn_left(self):
        new_orientation = (self.orientation[1], -self.orientation[0])
        self.orientation = new_orientation

        self.dot.moveTo(10 * self.orientation[0], 10 * self.orientation[1])


    def set_pause(self, delay):
        self.delay = delay


def create_world(avenues=10, streets=10):
    global world
    world = World(avenues, streets)


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

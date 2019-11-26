from cs1graphics import *
import time

world = None


class World:
    def __init__(self, avenues=10, streets=10):
        self.canvas = Canvas(avenues * 50 + 100, streets * 50 + 100)

    def add(self, robot):
        self.canvas.add(robot.layer)


class Robot:
    def __init__(self, color='gray', orientation='E', avenue=1, street=1):
        self.layer = Layer()
        self.layer.moveTo(avenue * 50 + 25, street * 50 + 25)

        self.body = Square(30)
        self.body.setFillColor(color)
        self.layer.add(self.body)

        self.dot = Circle(3)
        self.dot.setFillColor('black')
        self.layer.add(self.dot)

        world.add(self)


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

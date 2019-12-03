from cs1graphics import *

class Board:
    def __init__(self):
        self.canvas = Canvas(500, 500)
        self.player = Player(self, 250, 250)
        self.bullets = []

    def add(self, shape):
        self.canvas.add(shape)

    def update(self):
        e = self.canvas.wait()
        d = e.getDescription()
        if d == 'keyboard':
            key = e.getKey()
            if key == 'w':
                self.player.move(0, -10)
            elif key == 'a':
                self.player.move(-10, 0)
            elif key == 's':
                self.player.move(0, 10)
            elif key == 'd':
                self.player.move(10, 0)
        elif d == 'mouse click':
            p = e.getMouseLocation()
            vx = p.getX() - self.player.x
            vy = p.getY() - self.player.y
            self.bullets.append(Bullet(self, self.player.x, self.player.y, vx, vy))

    def fixedUpdate(self):
        for bullet in self.bullets:
            bullet.update()

class Player:
    def __init__(self, canvas, x, y):
        self.x = x
        self.y = y
        self.body = Square(20, Point(self.x, self.y))
        self.body.setFillColor('black')
        canvas.add(self.body)

    def move(self, dx, dy):
        self.body.move(dx, dy)
        self.x += dx
        self.y += dy

class Bullet:
    def __init__(self, canvas, x, y, vx, vy):
        self.vx = vx
        self.vy = vy
        self.shape = Circle(5, Point(x, y))
        canvas.add(self.shape)

    def update(self):
        self.shape.move(self.vx * 0.1, self.vy * 0.1)

board = Board()
while True:
    board.update()

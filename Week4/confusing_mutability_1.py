from cs1robots import *

def swap(x, y):
    x, y = y, x


world = create_world(10, 10)
robot1 = Robot(color = 'gray', avenue = 1, street = 1)
robot2 = Robot(color = 'blue', avenue = 1, street = 3)

swap(robot1, robot2)
robot1.move()


num1 = 57
num2 = 28

print(num1, num2)
swap(num1, num2)
print(num1, num2)

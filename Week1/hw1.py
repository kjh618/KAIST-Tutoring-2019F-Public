import math

a = 1
b = 2
c = 3

discriminant = b*b - 4*a*c

if discriminant >= 0:
    print((-b + math.sqrt(discriminant)) / 2)
    print((-b - math.sqrt(discriminant)) / 2)
else:
    print('Complex roots')

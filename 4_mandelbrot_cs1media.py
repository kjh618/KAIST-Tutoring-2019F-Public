from cs1media import *

black = (0, 0, 0)

def f(c, z):
    return z*z + c

def is_divergent(c):
    z = f(c, 0)
    for i in range(100):
        z = f(c, z)
        if abs(z) > 2:
            return True
    return False


re_start = -2
re_end = 2
num_re = 500
delta_re = (re_end - re_start) / num_re

im_start = 2
im_end = -2
num_im = 500
delta_im = (im_end - im_start) / num_im

image = create_picture(num_re, num_im, 'white')

for y in range(500):
    for x in range(500):
        re = re_start + x * delta_re
        im = im_start + y * delta_im
        c = re + im * 1j
        if not is_divergent(c):
            image.set(x, y, black)

image.show()

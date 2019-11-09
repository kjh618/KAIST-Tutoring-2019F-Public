from cs1media import *

def f(c, z):
    return z*z + c

def is_bounded(c, num_iter):
    z = 0
    for i in range(num_iter):
        z = f(c, z)
        if (abs(z) > 2):
            return False
    return True


re_start = -2
re_end = 2
num_re = 500
delta_re = (re_end - re_start) / num_re

im_start = 2
im_end = -2
num_im = 500
delta_im = (im_end - im_start) / num_im

image = create_picture(num_re, num_im, 'white')

im = im_start
for y in range(num_im):
    re = re_start
    for x in range(num_re):
        c = re + im*1j
        if is_bounded(c, 100):
            image.set(x, y, (0, 0, 0))
        re += delta_re

    im += delta_im

image.show()

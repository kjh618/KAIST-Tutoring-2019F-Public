from cs1media import *

img = load_picture("images/sunset.jpg")
w, h = img.size()

for y in range(h):
    for x in range(w):
        r, g, b = img.get(x, y)

        r = r // 16 * 16
        g = g // 16 * 16
        b = b // 16 * 16

        img.set(x, y, (r, g, b))

img.show()

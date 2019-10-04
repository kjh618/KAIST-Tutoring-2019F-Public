a = 1

def f(b):
    global a
    print(b)
    a = 2
    print(b)

f(a)

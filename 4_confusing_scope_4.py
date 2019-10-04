a = 1

def f():
    global a
    print(a)
    a = 2
    print(a)

f()

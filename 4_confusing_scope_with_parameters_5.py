a = 1

def g():
    print(a)

def f(a):
    print(a)
    a = 2
    g()

f(a)

a = 1

def f():
    global a
    a = 2

print(a)
f()
print(a)

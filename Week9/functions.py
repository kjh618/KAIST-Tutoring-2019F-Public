def f(a_list):
    sum = 0
    for a in a_list:
        sum += a
    return sum

def h(g, a_list):
    sum = 0
    for a in a_list:
        sum += g(a)
    return sum

def g(x):
    return 2 * x

a_list = [2, 4, 6, 8, 10]
print(f(a_list))
print(h(g, a_list))

def r(n):
    if n == 1:
        print(1, end=' ')
        return
    r(n - 1)
    print(n, end=' ')
    r(n - 1)

r(4)

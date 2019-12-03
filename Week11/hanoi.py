def hanoi(n, a, b):
    if n == 1:
        print(str(a) + ' -> ' + str(b))
        return
    hanoi(n-1, a, 6-a-b)
    hanoi(1, a, b)
    hanoi(n-1, 6-a-b, b)

hanoi(3, 1, 3)

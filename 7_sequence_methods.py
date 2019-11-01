def list_in(val, lst):
    for i in range(len(lst)):
        if lst[i] == val:
            return True
    return False


def list_index(self, val):
    for i in range(len(self)):
        if self[i] == val:
            return i
    return -1


def list_count(self, val):
    n = 0
    for i in range(len(self)):
        if self[i] == val:
            n = n + 1
    return n


def list_extend(self, lst):
    for i in range(len(lst)):
        self.append(lst[i])


def list_reverse(self):
    self1 = self[:]
    self.clear()
    for i in range(len(self1)):
        self.append(self1[-i-1])


lst1 = [10, 20, 20, 40, 30, 20, 30]
lst2 = [50, 10, 20, 30]

print(50 in lst1, list_in(50, lst1))
print(lst1.index(30), list_index(lst1, 30))
print(lst1.count(20), list_count(lst1, 20))
list_extend(lst1, lst2)
print(lst1)
list_reverse(lst1)
print(lst1)

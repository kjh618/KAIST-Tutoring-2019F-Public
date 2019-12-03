l = [113, 43, 13, 52, 53]

def calculateSum1(i):
    if i == 0:
        return l[i]
    return l[i] + calculateSum1(i-1)

def calculateSum2(i, sum):
    if i == len(l):
        return sum
    return calculateSum2(i+1, sum + l[i])

sum1 = 0
for i in range(len(l)):
    sum1 += l[i]

sum2 = calculateSum1(len(l) - 1)

sum3 = calculateSum2(0, 0)

print(sum1, sum2, sum3)

original = open('air_travel.csv', 'r')
transposed = open('air_travel_transposed.csv', 'w')

lines = []
for line in original:
    lines.append(line.strip().split(','))

for j in range(len(lines[0])):
    for i in range(len(lines)):
        if i == len(lines) - 1:
            transposed.write(lines[i][j] + '\n')
        else:
            transposed.write(lines[i][j] + ',')

original.close()
transposed.close()

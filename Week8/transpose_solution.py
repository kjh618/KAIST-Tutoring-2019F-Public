original = open('air_travel.csv', 'r')
transposed = open('air_travel_transposed.csv', 'w')

original_lines = []
for line in original:
    original_lines.append(line.strip().split(','))

original_num_rows = len(original_lines)
original_num_columns = len(original_lines[0])

transposed_lines = []
for _ in range(original_num_columns):
    transposed_lines.append([])

for i in range(original_num_rows):
    for j in range(original_num_columns):
        transposed_lines[j].append(original_lines[i][j])

for line in transposed_lines:
    transposed.write(','.join(line) + '\n')

print(original_lines)
print(transposed_lines)

original.close()
transposed.close()

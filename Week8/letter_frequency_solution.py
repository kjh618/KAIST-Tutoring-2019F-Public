alphabet = 'abcdefghijklmnopqrstuvwxyz'

file = open('wikipedia_color.txt', 'r', encoding='utf-8')

content = file.read().lower()

frequencies = {}
for letter in alphabet:
    frequencies[letter] = content.count(letter)

frequencies_sorted = []
for (key, value) in frequencies.items():
    frequencies_sorted.append((value, key))
frequencies_sorted.sort(reverse=True)

for f in frequencies_sorted:
    print('%s: %d' % (f[1], f[0]))

file.close()

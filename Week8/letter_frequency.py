file = open('wikipedia_color.txt', 'r', encoding='utf-8')

content = file.read().lower()

freq = {}

for letter in content:
    if letter not in 'abcdefghijklmnopqrstuvwxyz':
        continue
    if letter not in freq:
        freq[letter] = 1
    else:
        freq[letter] = freq[letter] + 1

print(sorted(freq.items()))

file.close()

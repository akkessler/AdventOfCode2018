def reducePolymer(polymer):
    i = 0
    while i < len(polymer)-1:
        x = polymer[i]
        y = polymer[i+1]
        if x.lower() == y.lower() and x != y:
            polymer = polymer[:i] + polymer[i+2:] # this removes x and y
            i = max(i-1, 0)
        else:
            i += 1
    return len(polymer)

f = open('input.txt', 'r')
line = f.read()
f.close()

min_length = len(line)
A_off = ord('A')
for x in range(26):
    letter = chr(A_off + x)
    polymer = line.replace(letter, '').replace(letter.lower(), '')
    length = reducePolymer(polymer)
    if length < min_length:
        min_length = length

print(min_length)
twos = 0
threes = 0
f = open('input.txt', 'r') 
for line in f:
    counts = {}
    for x in line.strip():
        if x not in counts:
            counts[x] = 1
        else:
            counts[x] += 1
    if 2 in counts.values():
        twos += 1
    if 3 in counts.values():
        threes += 1

print(twos * threes)
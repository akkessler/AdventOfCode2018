import numpy as np

twos = 0
threes = 0
a_off = ord('a') # used to index into array
f = open('input.txt', 'r') 
for line in f:
    counts = np.zeros(26) # would be more memory efficient to build a map from char to int
    for x in line.strip():
        counts[ord(x) - a_off] += 1 # this assumes line only contains a-z (lowercase)
    if 2 in counts:
        twos += 1
    if 3 in counts:
        threes += 1

print(twos * threes)
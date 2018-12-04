freq = 0
f = open('input.txt', 'r') 
for line in f: 
    freq += int(line)
print(freq)
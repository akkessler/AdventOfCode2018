freq = 0
f = open('input.txt', 'r') 
for line in f: 
    op = line[0]
    val = int(line[1:])
    if op is '-':
        freq -= val
    elif op is '+':
        freq += val
        
print(freq)
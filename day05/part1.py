f = open('input.txt', 'r')
line = f.read()
f.close()

i = 0
while i < len(line)-1:
    x = line[i]
    y = line[i+1]
    if x.lower() == y.lower() and x != y:
        line = line[:i] + line[i+2:] # this removes x and y
        i = max(i-1, 0)
    else:
        i += 1

print(len(line))
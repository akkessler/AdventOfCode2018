# Read input into memory since we may need to loop through change list multiple times.
changeList = []
f = open('input.txt', 'r') 
for line in f:
    changeList.append((line[0], int(line[1:])))
    
freq = 0
foundDup = False
seen = [freq] # Given example states the starting freq of 0 counts towards seen list
while not foundDup:
    for c in changeList:
        op = c[0]
        val = c[1]
        if op is '-':
            freq -= val
        elif op is '+':
            freq += val
        
        if freq in seen:
            foundDup = True
            break
        else:
            seen.append(freq)
            
print(freq)
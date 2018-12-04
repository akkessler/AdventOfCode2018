# Read input into memory since we may need to loop through change list multiple times.
changeList = []
f = open('input.txt', 'r') 
for line in f:
    changeList.append(int(line))
    
freq = 0
foundDup = False
seen = [freq] # Given example states the starting freq of 0 counts towards seen list
while not foundDup:
    for c in changeList:
        freq += c
        if freq in seen:
            foundDup = True
            break
        else:
            seen.append(freq)
            
print(freq)
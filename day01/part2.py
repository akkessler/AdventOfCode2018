def findDuplicateFrequency(changeList):
    freq = 0
    seen = [freq] # Given example states the starting freq of 0 counts towards seen list
    while True:
        for c in changeList:
            freq += c
            if freq in seen:
                return freq
            else:
                seen.append(freq)

# Read input into memory since we may need to loop through change list multiple times.
changeList = []
f = open('input.txt', 'r') 
for line in f:
    changeList.append(int(line))
                
dupFreq = findDuplicateFrequency(changeList)
print(dupFreq)
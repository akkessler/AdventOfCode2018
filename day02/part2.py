def findOffByOne(lines):
    length = len(lines[0].strip())
    for x in lines:
        for y in lines: # there is repeat checks, use index instead: `y in lines[#:]``
            diffs = 0
            index = -1
            for i in range(length):
                if x[i] != y[i]:  
                    diffs += 1
                    if diffs > 1:
                        break
                    index = i                  

            if diffs == 1:
                ans = ''
                for i in range(length):
                    if i != index:
                        ans += x[i]
                return ans 
    return ''


f = open('input.txt', 'r')
lines = f.readlines()
f.close()

answer = findOffByOne(lines)
print(answer)
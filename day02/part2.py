def findOffByOne(lines):
    length = len(lines[0].strip())
    for j in range(len(lines)):
        x = lines[j]
        for y in lines[j+1:]:
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
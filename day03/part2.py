import numpy as np
import re

def checkClaim(fabric, claim):
    rowStart = claim['rowStart']
    colStart = claim['colStart']
    for j in range(claim['rowSpan']):
        for i in range(claim['colSpan']):
            r = rowStart + j
            c = colStart + i
            if fabric[r][c] != 1:
                return False
    return True

regex = r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)"

f = open('input.txt', 'r') 
lines = f.readlines()
f.close()

claims = []
for line in lines:   
    m = re.match(regex, line)
    claim = {
        'id': int(m[1]),
        'colStart': int(m[2]),
        'rowStart': int(m[3]),
        'colSpan': int(m[4]),
        'rowSpan': int(m[5])
    }
    claims.append(claim)

fabric = np.zeros((1000,1000))
for claim in claims:
    rowStart = claim['rowStart']
    colStart = claim['colStart']
    for j in range(claim['rowSpan']):
        for i in range(claim['colSpan']):
            r = rowStart + j
            c = colStart + i
            fabric[r][c] += 1

# count = 0
# for r in range(fabric.shape[0]):
#     for c in range(fabric.shape[1]):
#         if fabric[r][c] > 1:
#             count += 1
# print(count)

for claim in claims:
    if checkClaim(fabric, claim):
        print('ID: {0}'.format(claim['id']))
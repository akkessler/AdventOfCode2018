import numpy as np

f = open('input.txt', 'r')
lines = f.readlines()
f.close()

deps = {}

for line in lines:
    letter1 = line[5]
    letter2 = line[36]
    if letter2 in deps:
        if letter1 not in deps[letter2]: # this prevents duplicate dependencies? prolly not needed
            deps[letter2].append(letter1)
    else:
        deps[letter2] = [letter1]

    if letter1 not in deps:
        deps[letter1] = []    

A_off = ord('A')
times = {}
for x in range(26):
    times[chr(A_off + x)] = 61 + x

order = ''
seconds = 0
max_workers = 5

free_steps = ['0'] # to get through first check of loop
in_progress = []
while len(free_steps) != 0:
    free_steps = []
    for key in deps:
        if len(deps[key]) == 0:
            free_steps.append(key)

    if len(free_steps) == 0:
        break

    free_steps.sort()
    for step in free_steps:
        if len(in_progress) < max_workers:
            if step not in in_progress:
                in_progress.append(step)
        else:
            break

    completed_steps = []
    while len(completed_steps) == 0:
        for step in in_progress:
            times[step] -= 1
            if times[step] == 0:
                completed_steps.append(step)
        seconds += 1

    for step in completed_steps:
        in_progress.remove(step)
        order += step
        for key in deps:
            if step in deps[key]:
                deps[key].remove(step)
        del deps[step]

print(order)
print(seconds)
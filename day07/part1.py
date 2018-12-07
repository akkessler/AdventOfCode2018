f = open('input.txt', 'r')
lines = f.readlines()
f.close()

answer = ''

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

free_steps = ['0'] # to get through first check of loop
while len(free_steps) != 0:
    free_steps = []
    for key in deps:
        if len(deps[key]) == 0:
            free_steps.append(key)

    if len(free_steps) > 0:
        free_steps.sort()
        step = free_steps[0] # must look for free steps again since we must go alphabetically
        answer += step
        for key in deps:
            if step in deps[key]:
                deps[key].remove(step)
        del deps[step]

print(answer)

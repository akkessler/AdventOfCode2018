f = open('input.txt', 'r')
line = f.read().split(' ')
x = [int(i) for i in line]
f.close()

i = 0
total = 0
while len(x) > 0:
    children = x[i]
    if children == 0:
        metas = x[i+1]
        meta_start = i+2
        meta_end = meta_start + metas
        total += sum(x[meta_start:meta_end])
        del x[i:meta_end]
        i -= 2
        try:
            x[i] -= 1
        except IndexError as ex: # this happens once we are done
            print(total)
            break
    else:
        i += 2
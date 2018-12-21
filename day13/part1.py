# import numpy as np
# grid = np.chararray((rows, cols)) 

# order is important since these are parallel arrays
turn_cycle = [-1, 0, 1]
cart_chars = ['<','^','>','v']
track_chars = ['-','|','-','|']
backward_curve = ['^', '<', 'v', '>']
forward_curve = ['v','>','^','<']
dirs = [(0,-1),(-1,0),(0,1),(1,0)]
def simulate_carts(grid, carts):
    while True: # will return with coords tuple once collision occurs
        # 1) Sort cart list by row (top to bottom) then column (left to right).
        carts = sorted(carts, key = lambda x: (x['row'], x['col']))
        # 2) Iterate through cart list, move 1 step in direction of cart
        for c in carts:
            index = c['cart']       
            vector = dirs[index]
            new_r = c['row'] + vector[0]
            new_c = c['col'] + vector[1]
            new_char = grid[new_r][new_c]
            # 3) If new location has another cart, return new coords.
            if new_char in cart_chars: # COLLISION
                return (new_r, new_c)
            new_index = index
            # 4) If new location has \ / or + then make turn and update cart's state accordingly
            if new_char == '/':
                new_index = cart_chars.index(forward_curve[index])
            elif new_char == '\\':
                new_index = cart_chars.index(backward_curve[index])
            elif new_char == '+':
                turnIndex = c['turnIndex']
                new_index = (index + turn_cycle[turnIndex]) % 4
                c['turnIndex'] = (turnIndex + 1) % 3
            grid[c['row']][c['col']] = c['track'] # put back old track piece
            grid[new_r][new_c] = cart_chars[new_index] # update new track piece with cart
            c['cart'] = new_index # stores cart orientation
            c['track'] = new_char # remember track piece this cart is on, to replace later ^^^
            c['row'] = new_r
            c['col'] = new_c
f = open('input.txt', 'r')
lines = f.readlines()
f.close()
rows = len(lines)
cols = len(lines[0]) - 1 # include whitespace, exclude \n
grid = [] # figure out why numpy isn't working.
carts = []
for r in range(rows):
    row = []
    line = lines[r].replace('\n','')
    for c in range(cols):
        char = line[c]
        if char in cart_chars:
            index = cart_chars.index(char)
            carts.append({
                'row': r, # y
                'col': c, # x
                'cart': index, # can use this index to direction and other arrays
                'track': track_chars[index],
                'turnIndex': 0 # start at 0
            })
        row.append(char)
    grid.append(row)
coords = simulate_carts(grid, carts)
print(coords) # outputs as (r,c). AoC site wants it in form (x,y) or in this case (c,r).
import numpy as np

f = open('input.txt', 'r')
line = f.read().split() # "466 players; last marble is worth 71436 points"
f.close()

players = int(line[0])
max_marble = int(line[-2])

points = np.zeros(players)

# starting with first 2 marbles in to remove complexity on 0 case
marbles = [0, 1] 
curr_index = 1
next_marble = 2
player = 1

while next_marble <= max_marble:
    # print(curr_index, marbles)
    if next_marble % 23 == 0:
        next_index = (curr_index - 7) % len(marbles)
        points[player] += next_marble + marbles[next_index]
        del marbles[next_index]
        curr_index = next_index % len(marbles)
    else:
        next_index = curr_index + 2
        if next_index == len(marbles):
            marbles.append(next_marble)
        else:
            next_index %= len(marbles)
            marbles.insert(next_index, next_marble)
        curr_index = next_index % len(marbles)
    next_marble += 1
    player = (player + 1) % players

print(int(np.max(points)))
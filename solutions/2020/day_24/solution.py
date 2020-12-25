from collections import defaultdict, Counter, deque
import numpy as np
# import re
import os, sys

def read_input(filename='input.txt'):
    with open(os.path.join(os.getcwd(),filename)) as f:
        result = list()
        for line in f.readlines():
            result.append(line.rstrip())
        return result

if len(sys.argv) == 2:
    inputText = read_input(sys.argv[1])
else:
    inputText = read_input()

def parse_input(inputText):
    directions = list()
    newDirection = True
    for d in inputText:
        directions.append(list())
        for s in d:
            if newDirection:
                directions[-1].append('')
                directions[-1][-1] += (s)
                if s in 'ew':
                    newDirection = True
                else:
                    newDirection = False
            else:
                directions[-1][-1] += (s)
                newDirection = True

    return directions

def move(x,y, delta, c):
    return x + c * delta[0], y + c * delta[1]

def conway(lobby):
    temp = lobby.copy()
    rows, cols = lobby.shape

    d ={True:1, False:0}

    for r in range(2,rows-2):
        for c in range(2,cols-2):
            if (r+c)%2 != 0: continue
            adjacents = 0
            adjacents = d[lobby[r-1, c-1]] + d[lobby[r-1, c+1]] + \
                          d[lobby[r, c-2]] + d[lobby[r, c + 2]] + \
                          d[lobby[r+1, c-1]] + d[lobby[r+1, c+1]]
            # Any black tile with zero or more than 2 black tiles immediately adjacent 
            # to it is flipped to white.
            if lobby[r,c]:
                if adjacents == 0 or adjacents > 2:
                    temp[r,c] = False
            # Any white tile with exactly 2 black tiles
            #  immediately adjacent to it is flipped to black.
            else:
                if adjacents == 2:
                    temp[r,c] = True
    return temp

def part_1():
    tileDirections = parse_input(inputText)
    seen = defaultdict(int)
    transform = {'e': (2,0),
                 'w': (-2,0),
                 'ne': (1,1),
                 'nw': (-1,1),
                 'se': (1,-1),
                 'sw': (-1,-1)
                 }
    for tile in tileDirections:
        x, y = 0,0
        for d, c in Counter(tile).items():
            x, y = move(x,y, transform[d], c)
        seen[(x,y)] += 1
    
   
    return seen

def part_2(blacks):
    # xmax, ymax    (28, 14)
    # xmin, ymin    (-25, -14)
    size = 301
    x0, y0 = size//2 + 1, size//2 + 1 
    days = 100
    lobby = np.array(size*size*[False]).reshape(size,size)
    
    for b in blacks:
        lobby[x0 + b[1], y0 + b[0]] = True

    for day in range(days):
        # print('Day ', day, ': ', sum(sum(lobby)))
        lobby = conway(lobby).copy()

    result = sum(sum(lobby))
    print('Day ', day, ': ', result )

    return result

seen = part_1()
blacks = [tile for tile, color in seen.items() if color%2 == 1]
whites = [tile for tile, color in seen.items() if color%2 == 0]

print('\n=========================\nPart 1: ', len(blacks))

print('\n=========================\nPart 2: ')
print(part_2(blacks))
from collections import defaultdict, Counter, deque
# import numpy as np
# import re
import os, sys

def read_input(filename='test.txt'):
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
    
    print(seen)

    blacks = [tile for tile, color in seen.items() if color%2 == 1]
    whites = [tile for tile, color in seen.items() if color%2 == 0]
    
    return len(blacks)

def part_2():
    pass

print('\n=========================\nPart 1: ', part_1())

print('\n=========================\nPart 2: ', part_2())
# prompt: https://adventofcode.com/2020/day/19

# from collections import defaultdict
# import numpy as np
# import re
import sys

def read_input(filename='input.txt'):
    with open(filename) as f:
        result = list()
        for line in f.readlines():
            result.append(line.rstrip())
        return result

if len(sys.argv) == 2:
    inputText = read_input(sys.argv[1])
else:
    inputText = read_input()

def read_Tile(i, inputText):
    tileName = int(inputText[i][-5:-1])
    sides = list()
    sides.append(inputText[i+1].replace('.','0').replace('#','1'))
    sides.append(inputText[i+10].replace('.','0').replace('#','1'))
    sides.append(''.join([inputText[i+c][0].replace('.','0').replace('#','1') for c in range(1,11)]))
    sides.append(''.join([inputText[i+c][-1].replace('.','0').replace('#','1') for c in range(1,11)]))
    
    result = list()
    for s in sides:
        result.append(int(s,2))
        result.append(int(''.join(reversed(s)),2))
    
    return tileName, result

def part_1() -> int:
    tiles = dict()
    for i, line in enumerate(inputText):
        if line == '':continue
        if 'Tile' in line:
            tileName, content = read_Tile(i, inputText)
            tiles[tileName] = content
    
    tileNames = tiles.keys()

    result = 1
    for tileName, sides in tiles.items():
        adjacents = 0
        for side in sides:
            adjacents += sum([True if side in tiles[i] else False for i in tileNames if i != tileName])
        if adjacents == 4:
            result *= tileName
            print(tileName, adjacents)

    return result
# 1951    2311    3079
# 2729    1427    2473
# 2971    1489    1171

# 20899048083289

def part_2() -> int:
    pass

print('\n================\nPart 1: ', part_1())
print('\n================\nPart 2: ', part_2())

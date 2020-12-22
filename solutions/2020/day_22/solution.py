from collections import defaultdict, deque
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

def part_1():
    decks = list()
    for line in inputText:
        if 'Player' in line:
            decks.append(deque())
        elif line == '':
            continue
        else:
            decks[-1].append(int(line))

    print('Player 1: ', decks[0]) 
    print('Player 2: ', decks[1]) 

    player_1 = decks[0]
    player_2 = decks[1]

    while True:
        card1 = player_1.popleft()
        card2 = player_2.popleft()

        if card1 > card2:
            player_1.append(card1)
            player_1.append(card2)
        elif card2 > card1:
            player_2.append(card2)
            player_2.append(card1)
        elif card1 == card2:
            print('This should not happen!')
            break

        if len(player_1) == 0 or len(player_2) == 0:
            break

    if len(player_1) == 0:
        winner = player_2
    else:
        winner = player_1

    result = 0
    for i, c in enumerate(winner):
        result += (len(winner) - i) * c

    return result

def part_2():
    pass

print('\n=========================\nPart 1: ', part_1())
print('\n=========================\nPart 2: ', part_2())
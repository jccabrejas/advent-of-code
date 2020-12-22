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

def parse_input(inputText):
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

    return player_1, player_2

def game_round(player_1, player_2):
    card1 = player_1.popleft()
    card2 = player_2.popleft()

    if card1 > card2:
        player_1.append(card1)
        player_1.append(card2)
    elif card2 > card1:
        player_2.append(card2)
        player_2.append(card1)

    return player_1, player_2

def game(player_1, player_2, _):
    while True:
        player_1, player_2 = game_round(player_1, player_2)

        if len(player_1) == 0 or len(player_2) == 0:
            break

    if len(player_1) == 0:
        winner = 2
    else:
        winner = 1
    
    return winner

def recursive_game(player_1, player_2, depth):
    print('Game ', depth + 1)
    print('Player 1s deck: ', player_1)
    print('Player 2s deck: ', player_2)

    seen = [[player_1.copy(), player_2.copy()]]
    while True:
        if len(player_1) == 0:
            winner = 2
            return winner
        if len(player_2) == 0:
            winner = 1
            return winner
        if (len(player_1) - 1 >= player_1[0]) and (len(player_2) - 1 >= player_2[0]):
            temp1 = player_1.copy()
            temp1.popleft()
            while len(temp1) != player_1[0]:
                temp1.pop()
            temp2 = player_2.copy()
            temp2.popleft()
            while len(temp2) != player_2[0]:
                temp2.pop()

            winner = recursive_game(temp1, temp2, depth + 1)
            if winner == 1:
                player_1.append(player_1.popleft())
                player_1.append(player_2.popleft())
            elif winner == 2:
                player_2.append(player_2.popleft())
                player_2.append(player_1.popleft())
        else:
            player_1, player_2 = game_round(player_1, player_2)
        
        for s in seen:
            if [player_1, player_2] == s:
                winner = 1
                return winner
        seen.append([player_1.copy(), player_2.copy()])

    return winner

def play(f, player_1, player_2):

    winner = f(player_1, player_2, 0)
    
    if winner == 1:
        winner_player = player_1
    else:
        winner_player = player_2
    
    result = 0
    for i, c in enumerate(winner_player):
        result += (len(winner_player) - i) * c

    return result


player_1, player_2 = parse_input(inputText)
print('\n=========================\nPart 1: ', play(game, player_1, player_2))

player_1, player_2 = parse_input(inputText)
print('\n=========================\nPart 2: ', play(recursive_game, player_1, player_2))
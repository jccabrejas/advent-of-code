from collections import defaultdict, deque
# import numpy as np
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
    return int(inputText[0]), int(inputText[1])

def transform(value, subjectNumber):
    value *= subjectNumber
    value = value%20201227
    return value

def find_loop_size(PublicKey):
    value = 1
    LoopSize = 0

    subjectNumber = 7

    while True:
        LoopSize +=1
        value = transform(value, subjectNumber)
        if value == PublicKey:
            break
    return LoopSize

def part_1():
    cardPublicKey, doorPublicKey = parse_input(inputText)

    cardLoopSize = find_loop_size(cardPublicKey)
    doorLoopSize = find_loop_size(doorPublicKey)

    value = 1
    subjectNumber = doorPublicKey
    for _ in range(cardLoopSize):
        value = transform(value, subjectNumber)

    keyFromCard = value

    value = 1
    subjectNumber = cardPublicKey

    for _ in range(doorLoopSize):
        value = transform(value, subjectNumber)

    keyFromDoor = value

    assert(keyFromCard == keyFromDoor)
    
    return keyFromCard
    

def part_2():
    pass

print('\n=========================\nPart 1: ', part_1())

print('\n=========================\nPart 2: ', part_2())
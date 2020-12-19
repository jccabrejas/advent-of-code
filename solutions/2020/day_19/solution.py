# prompt: https://adventofcode.com/2020/day/19

from collections import defaultdict
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

def substitute(item):
    result = list()

    if all([True if x in 'ab' else False for x in item]):
        for i in item:
            result.append(rules[i])
        return result
    else:
        for i, x in enumerate(item):
            if type(x) == str: continue
            if all([True if type(y) == str else False for y in x]):
                result[i] = substitute(x)
            else:
                result[i] = self.not_simple(x, f)

def part_1() -> int:
    rules = defaultdict(list)
    messages = list()

    for line in inputText:
        # 2: 4 4 | 5 5
        if line == '':
            continue
        elif '"a"' in line:
            a = line.split(':')[0]
            rules[a] = 'a'
        elif '"b"' in line:
            b = line.split(':')[0]
            rules[b] = 'b'
        elif '|' in line:
            ruleNumber, ruleTemp = line.split(':')
            r1, r2 = ruleTemp.split('|')
            _, r11, r12, _ = r1.split(' ')
            _, r21, r22 = r2.split(' ')
            rules[ruleNumber] = [[r11,r12], [r21,r22]]
            continue
        elif ':' in line:
            ruleNumber, ruleTemp = line.split(':')
            rules[ruleNumber] = ruleTemp.split(' ')[1:]
        else:
            messages.append(line)

    print(rules)
    print(messages)

    for v in rules[0]:
            result = substitute(v)

def part_2() -> int:
    pass

print('\n================\nPart 1: ', part_1())
print('\n================\nPart 2: ', part_2())

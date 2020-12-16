# prompt: https://adventofcode.com/2020/day/16

from ...base import BaseSolution, InputTypes
from collections import defaultdict
# from typing import Tuple

class Solution(BaseSolution):
    year = 2020
    number = 16
    input_type = InputTypes.STRSPLIT

    # def part_1(self) -> int:
    #     pass

    # def part_2(self) -> int:
    #     pass

    def ruleApplies(self, field, validRanges):
        
        for validRange in validRanges:
            if validRange[0] <= field <= validRange[1]:
                return True 
        return False

    def solve(self) -> tuple((int, int)):
        rules = defaultdict(list)
        tickets = list()
        # read rules
        # class: 1-3 or 5-7
        flagRules, flagYours, flagNearby  = True, False, False

        # Parse input => tickets and rules
        for line in self.input:
            if line == '':
                continue
            elif line == 'your ticket:':
                flagRules, flagYours, flagNearby = False, True, False
                continue
            elif line == 'nearby tickets:':
                flagRules, flagYours, flagNearby  = False, False, True 
                continue

            if flagRules:
                ruleName, ruleText = line.split(':')
                _1, rule1, _2, rule2 = ruleText.split(' ')
                r1F, r1T = rule1.split('-')
                r2F, r2T = rule2.split('-')
                rules[ruleName] = [[], []]
                rules[ruleName][0].append(int(r1F))
                rules[ruleName][0].append(int(r1T))
                rules[ruleName][1].append(int(r2F))
                rules[ruleName][1].append(int(r2T))

            elif flagYours:
                fields = [int(s) for s in line.split(',')]
                tickets.append(fields)

            elif flagNearby:
                fields = [int(s) for s in line.split(',')]
                tickets.append(fields)

        resultPart1 = 0
        validTickets = list()
        # remove invalid tickets
        for ticket in tickets:
            isValidTicket = True
            for field in ticket:
                isValidField = False
                for ruleName, validRanges in rules.items():
                    for validRange in validRanges:
                        if validRange[0] <= field <= validRange[1]:
                            isValidField = True
                    
                if not isValidField:
                    resultPart1 += field
                    isValidTicket = False
            
            if isValidTicket:
                validTickets.append(ticket)

        # for each valid ticket
        #     for each field
        #         set of possible classes

        allRules = set(rules.keys())
        t = 0
        possible = defaultdict(list)
        fieldPossible = list()

        # find possible rules for each field in each ticket
        for ticket in validTickets:
            f = 0
            for field in ticket:
                possible[t].append(list())
                for ruleName, validRanges in rules.items():
                    if self.ruleApplies(field, validRanges):
                        possible[t][f].append(ruleName)
                f += 1            
            t += 1

        # for each field, find possible rules across all tickets
        fieldRules = list()
        for f in range(len(possible[0])):
            start = allRules.copy()
            for ticket, possibleRules in possible.items():
                start = set.intersection(start, possibleRules[f])
            fieldRules.append(start)

        summary = dict()
        result = fieldRules.copy()

        while True:
            fieldRules = result.copy()
            for i, f in enumerate(fieldRules):
                if len(f) == 1:
                    summary[i] = f
                    result = [r - f for r in result]
            if result == fieldRules:
                break

        print(summary)

        solution = 1

        for k, v in summary.items():
            if next(iter(v)).startswith('departure'):
                solution *= tickets[0][k]

        return resultPart1, solution

# possible rules for each ticket and field
# 3,9,18   0: [ [  r s], [c r s], [c r s] ] 
# 15,1,5   1: [ [c r  ], [c r s], [c r s] ]
# 5,14,9   2: [ [c r s], [c r  ], [c r s] ]

# intersection by field
#                  r      c r      c r s
# Eliminate known solutions in each iteration
#                  r      c        c   s
#                  r      c            s

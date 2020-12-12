# prompt: https://adventofcode.com/2020/day/10

from ...base import BaseSolution, InputTypes
# from typing import Tuple
from itertools import permutations, combinations

class Solution(BaseSolution):
    year = 2020
    number = 10
    input_type = InputTypes.INTSPLIT

    def check_chain(self, adapters):
        # True if valid chain (3 or less between adjacent items)
        # Otherwise False
        prev = 0
        for i in range(len(adapters)):
            if adapters[i] - prev < 4:
                prev = adapters[i]
                continue
            else:
                return False
        return True

    def alone(self, indexes):
        # identify items that can be taken out for sure as they are
        # surrounded by items which can not be taken out
        result = []

        for i in range(1, len(indexes)-1):
            if indexes[i+1] - indexes[i] != 1 and indexes[i] - indexes[i-1] != 1:
                result.append(i)  
        return result

    def part_1(self) -> int:
        adapters = sorted(self.input)
        ones = 0
        twos = 0
        threes = 0
        prev = 0
        for i in range(len(adapters)):
            if adapters[i] - prev == 1:
                ones += 1
                prev = adapters[i]
                continue
            elif adapters[i] - prev == 2:
                twos += 1
                prev = adapters[i]
                continue
            elif adapters[i] - prev == 3:
                threes += 1
                prev = adapters[i]
                continue
            else:
                return False
            
        threes += 1
        
        return ones, twos, threes, ones * threes

    def part_2(self) -> int:
        adapters = sorted(self.input)
        can_be_removed = []
        indexes = []
        prev = 0
        # Find list of items that can be removed and the corresponding indexes
        for i in range(len(adapters)-1):
            if adapters[i+1] - prev <= 3:
                can_be_removed.append(adapters[i])
                indexes.append(i)
            prev = adapters[i]

        print('All: ', adapters)
        print('Can be removed: ', can_be_removed)
        print('Indexes: ', indexes)
        print('Alones:' , self.alone(indexes))

        # Divide list in list of segments, each having adjacent items
        segments = []
        segcounter = 0
        startcounter = 0
        for i in range(len(indexes)-1):
            if indexes[i+1] - indexes[i] == 1:
                continue
            segments.append(indexes[startcounter:i+1])
            startcounter = i+1
        segments.append(indexes[startcounter:])

        print(segments)
        print(len(indexes))

        # Island items can always be taken, so total number of 
        # combinations is 2**(number of island items) 
        ones = 0
        for s in segments:
            if len(s) == 1:
                ones +=1
                segments.remove(s)

        # For the longer segments, find the valid combinations 
        # for each segment (remove items and check)
        segmentcombinations = []

        for s in segments:
            result = 1
            for j in range(len(s)):
                for c in combinations(s, j+1):
                    temp = adapters.copy()
                    for i in c:
                    # print(temp, 'c', c, 'i', i, adapters[i])
                        temp.remove(adapters[i])
                    result += self.check_chain(temp)
            segmentcombinations.append(result)

        print(segmentcombinations)

        # Multiply all combinations
        result = 1
        for i in segmentcombinations:
            result *= i
        return result * 2**ones

#   def solve(self) -> Tuple[int, int]:
#       pass

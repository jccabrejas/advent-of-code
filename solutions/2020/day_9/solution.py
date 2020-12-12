# prompt: https://adventofcode.com/2020/day/9

from ...base import BaseSolution, InputTypes
# from typing import Tuple
from collections import deque
from itertools import permutations

class Solution(BaseSolution):
    year = 2020
    number = 9
    input_type = InputTypes.STRSPLIT

    def can_be_added(self, history, n):
        for i, j in permutations(history,2):
            if i + j == n: return True
        return False

    def part_1(self) -> int:
        preamble_legnth = 25
        history = deque(maxlen=preamble_legnth)
        for n in range(preamble_legnth):
            history.append(int(self.input[n]))

        # print(history)

        for n in range(preamble_legnth, len(self.input)):
            next_value = int(self.input[n]) 
            if self.can_be_added(history, next_value):
                history.append(next_value)
                continue
            else:
                return next_value
        
        print ('Everything fine!')
        return next_value

    def part_2(self) -> int:
        target = self.part_1()
        
        for i in range(len(self.input)):
            result = int(self.input[i])
            active_range = deque()
            active_range.append(int(self.input[i]))

            for j in range(i+1, len(self.input)):
                active_range.append(int(self.input[j]))
                result += int(self.input[j])
                if result == target:
                    return min(active_range) + max(active_range)


#   def solve(self) -> Tuple[int, int]:
#       pass

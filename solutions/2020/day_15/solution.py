# prompt: https://adventofcode.com/2020/day/15

from ...base import BaseSolution, InputTypes
# from typing import Tuple
from collections import defaultdict

class Solution(BaseSolution):
    year = 2020
    number = 15
    input_type = InputTypes.STRSPLIT

    def part_1(self) -> int:
        sequence = [int(x) for x in self.input[0].split(',')]
        last = sequence[-1]
        sequence.pop(-1)
        seen = defaultdict(list)

        for idx, value in enumerate(sequence):
            seen[int(value)].append(idx+1)

        counter = len(sequence)
        counter += 2

        while counter <= 30000000:
            if last not in seen:
                last = 0
                seen[0].append(counter)
                print(0)
            else:
                diff = seen[last][-1] - seen[last][-2]
                seen[diff].append(counter)
                last = diff
                print(last)
            counter +=1

        return last

    def part_2(self) -> int:
        pass

#   def solve(self) -> Tuple[int, int]:
#       pass

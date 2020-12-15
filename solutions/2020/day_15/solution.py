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
        seen = defaultdict(list)

        for idx, value in enumerate(sequence):
            seen[int(value)].append(idx+1)

        counter = len(sequence)
        counter += 1

        while counter <= 2020:
            if (last := sequence[-1]) not in sequence[:-1]:
                sequence.append(0)
                seen[0].append(counter)
            else:
                diff = seen[last][-1] - seen[last][-2]
                sequence.append(diff)
                seen[diff].append(counter)

            counter +=1

        return sequence[-1]

    def part_2(self) -> int:
        pass

#   def solve(self) -> Tuple[int, int]:
#       pass

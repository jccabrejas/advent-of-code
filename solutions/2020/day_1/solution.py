# prompt: https://adventofcode.com/2020/day/1

from ...base import BaseSolution, InputTypes
# from typing import Tuple

import itertools

class Solution(BaseSolution):
    year = 2020
    number = 1
    input_type = InputTypes.INTSPLIT

    def part_1(self) -> int:
        for x, y in itertools.combinations(self.input, 2):
            if x + y == 2020: return(x*y) 

    def part_2(self) -> int:
        for x, y, z in itertools.combinations(self.input, 3):
            if x + y + z == 2020: return (x*y*z) 

#   def solve(self) -> Tuple[int, int]:
#       pass

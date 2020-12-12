# prompt: https://adventofcode.com/2020/day/5

from ...base import BaseSolution, InputTypes
# from typing import Tuple
import math

class Solution(BaseSolution):
    year = 2020
    number = 5
    input_type = InputTypes.STRSPLIT

    def binary(self, char, min_val, max_val):
        middle_value = min_val + (max_val - min_val)/2

        if char in 'FL': # lower half
            return min_val, math.floor(middle_value)
        if char in 'BR': # upper half
            return math.ceil(middle_value), max_val

    def part_1(self) -> int:

        IDs = []
        for seat in self.input:
            min_val, max_val = 0, 127
            for char in seat[0:7]:
                min_val, max_val = self.binary(char, min_val, max_val)
            row = min_val
            min_val, max_val = 0, 7
            for char in seat[7:10]:
                min_val, max_val = self.binary(char, min_val, max_val)
            col = min_val
            ID = row * 8 + col
            print('Seat ', seat[0:10], ' Row: ', row, ' Col: ', col, ' => ', ID)

            IDs.append(ID)
        
        print('Max ID:', max(IDs))

        return IDs

    def part_2(self) -> int:
        IDlist = sorted(self.part_1())
        IDs = set(IDlist)
        possible_IDs = set([r*8+c for r in range(127) for c in range(7)])
        empty_seats = possible_IDs - IDs
        # print('IDs:', len(IDs), sorted(IDs))
        prev = IDlist[0]
        for s in IDlist[1:]:
            if s != prev + 1:
                print('Your seat is ', prev + 1)
                print(empty_seats)
                break
            prev = s
        return prev + 1

#   def solve(self) -> Tuple[int, int]:
#       pass

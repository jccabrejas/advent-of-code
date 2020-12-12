# prompt: https://adventofcode.com/2020/day/3

from ...base import BaseSolution, InputTypes
# from typing import Tuple
from collections import deque

class Solution(BaseSolution):
    year = 2020
    number = 3
    input_type = InputTypes.STRSPLIT


    def part_1(self) -> int:
        right = 3
        down = 1

        trees = 0

        line_counter = 0
        # t = [print(x) for x in self.input]

        for line in self.input:
            
            if line_counter == 0:
                # print(line_counter, line)
                line_counter += 1
                continue
            line_deque = deque(line)
            line_deque.rotate(-right*line_counter)
            # print(line_counter, line_deque)
            if line_deque[0] == '#':
                trees +=1
            line_counter += 1
        return trees

    def part_2(self) -> int:
        # 1,1 => 60
        # 3,1 => 386
        # 5,1 => 76
        # 7,1 => 62
        # 1,2 => 45

        slopes = [[1,1], [3,1], [5,1], [7,1], [1,2]]

        result = []

        for right, down in slopes:
            print(right, down)

            trees = 0

            line_counter = 0
            right_counter = 0
            # t = [print(x) for x in self.input]

            for line in self.input:
                
                if line_counter == 0:
                    line_counter += 1
                    right_counter += 1
                    continue
                if down != 1 and ((line_counter-1) % 2 == 0):
                    line_counter += 1
                    continue
                line_deque = deque(line)
                line_deque.rotate(-right*right_counter)
                if line_deque[0] == '#':
                    trees +=1
                line_counter += 1
                right_counter += 1
            
            result.append(trees)

        final = 1
        for i in result:
            final = final * i
        print(result) 
        return final
        

#   def solve(self) -> Tuple[int, int]:
#       pass

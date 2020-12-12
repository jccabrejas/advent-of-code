# prompt: https://adventofcode.com/2020/day/6

from ...base import BaseSolution, InputTypes
# from typing import Tuple
from collections import Counter

class Solution(BaseSolution):
    year = 2020
    number = 6
    input_type = InputTypes.STRSPLIT
    separator = '\n\n'

    def part_1(self) -> int:
        print(len(self.input))
        result = 0
        for group in self.input:
            groupCount = Counter(group)
            if '\n' in groupCount.keys(): 
                groupCount.pop('\n')
            questionCount = Counter(groupCount.keys())
            print(group)
            print(sum(questionCount.values()))
            result += sum(questionCount.values())
        return result


    def part_2(self) -> int:
        # read group
        result = 0
        for group in self.input:
            groupPersons = list()
            for person in group.split('\n'):
                personQuestion = set([q for q in person])
                groupPersons.append(personQuestion)
            print(groupPersons)

            result += len(set.intersection(*groupPersons))
        return result
        # split by person
        # count per person
        # intersection for group
        pass

#   def solve(self) -> Tuple[int, int]:
#       pass

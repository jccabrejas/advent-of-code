# prompt: https://adventofcode.com/2020/day/8

from ...base import BaseSolution, InputTypes
# from typing import Tuple

class Solution(BaseSolution):
    year = 2020
    number = 8
    input_type = InputTypes.STRSPLIT

    def does_terminate(self, program):
        index = 0
        counter = 0
        seen = list()
        while index < len(program):
            seen.append(index)
            action, value = program[index].split(' ')
            value = int(value)
            if action == 'nop':
                index += 1
                if index in seen:
                    return counter, False
            if action == 'acc':
                index += 1
                if index in seen:
                    return counter, False
                counter += value
                continue
            if action == 'jmp':
                index += value
                if index in seen:
                    return counter, False
                continue

        return counter, True

    def part_1(self) -> int:
        index = 0
        counter = 0
        seen = list()
        while True:
            seen.append(index)
            action, value = self.input[index].split(' ')
            value = int(value)
            if action == 'nop':
                index += 1
                if index in seen:
                    break
                continue
            if action == 'acc':
                index += 1
                if index in seen:
                    break
                counter += value
                continue
            if action == 'jmp':
                index += value
                if index in seen:
                    break
                continue

        return counter

    def part_2(self) -> int:

        for i in range(len(self.input)):
            print(i)
            if self.input[i].split(' ')[0] == 'acc': continue

            if self.input[i].split(' ')[0] == 'nop':
                program = list()
                program = self.input.copy()
                program[i] = program[i].replace('nop', 'jmp')
                counter, success = self.does_terminate(program)
                if success: return counter
            
            if self.input[i].split(' ')[0] == 'jmp':
                program = list()
                program = self.input.copy()
                program[i] = program[i].replace('jmp', 'nop')
                counter, success = self.does_terminate(program)
                if success: return counter


#   def solve(self) -> Tuple[int, int]:
#       pass

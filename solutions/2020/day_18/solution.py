# prompt: https://adventofcode.com/2020/day/18

from ...base import BaseSolution, InputTypes
# from typing import Tuple

class Solution(BaseSolution):
    year = 2020
    number = 18
    input_type = InputTypes.STRSPLIT

    def parse_to_list(self, s, j):
        result = list()

        for i, c in enumerate(s):
            if i<j: continue
            if c == ' ': continue
            if c in '+*0123456789':
                result.append(c)
            elif c == '(':
                r, j = self.parse_to_list(s, i+1)
                result.append(r)
            elif c == ')':
                return result, i+1
        return result, i+j

    def simple(self, expression):
        if len(expression) == 3:
            return str(eval(''.join(expression)))
        else:
            return str(eval(self.simple(expression[:-2])+''.join(expression[-2:])))

    def mixed(self, expression):
 
        r = 0
        temp = list()
        # temp.append(expression[0])
        flag = False
        for i, x in enumerate(expression):
            if flag: 
                flag = False
                continue
            if x == '+':
                temp[-1] = str(int(temp[-1]) + int(expression[i+1]))
                flag = True
            else:
                temp.append(x)

        if len(temp) == 1:
            return temp[0]
        else:
            result = 1
            for i in range(0,len(temp),2):
                result *= int(temp[i])
            return str(result)

    def not_simple(self, item):
        if all([True if type(x) == str else False for x in item]):
            return self.simple(item)
        else:
            result = item.copy()
            for i, x in enumerate(item):
                if type(x) == str: continue
                if all([True if type(y) == str else False for y in x]):
                    result[i] = self.simple(x)
                else:
                    result[i] = self.not_simple(x)
            
            return self.not_simple(result)

    def not_mixed(self, item):
        if all([True if type(x) == str else False for x in item]):
            return self.mixed(item)
        else:
            result = item.copy()
            for i, x in enumerate(item):
                if type(x) == str: continue
                if all([True if type(y) == str else False for y in x]):
                    result[i] = self.mixed(x)
                else:
                    result[i] = self.not_mixed(x)
            
            return self.not_mixed(result)


    def part_1(self) -> int:
        s = '((2+4*9)*(6+9*8+6)+6)+2+4*2'
        s = '5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))'

        result = 0
        for line in self.input:
            parsed, _ = self.parse_to_list(line, 0)
            result += int(self.not_simple(parsed))
        return result

    def part_2(self) -> int:
        s = '1 + 2 * 3 + 4 * 5 + 6'
        result = 0
        for line in self.input:
            parsed, _ = self.parse_to_list(line, 0)
            result += int(self.not_mixed(parsed))
        return result


#   def solve(self) -> Tuple[int, int]:
#       pass

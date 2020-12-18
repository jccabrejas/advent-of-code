# prompt: https://adventofcode.com/2020/day/18

from ...base import BaseSolution, InputTypes

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

    @staticmethod
    def left_to_right(expression, f):
        if len(expression) == 3:
            return str(eval(''.join(expression)))
        else:
            return str(eval(f(expression[:-2], f)+''.join(expression[-2:])))

    @staticmethod
    def reversed_op_precedence(expression, f):
 
        r = 0
        temp = list()

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
    
    def not_simple(self, item, f):
        # f can be either left_to_right or reversed_op_precedence

        if all([True if type(x) == str else False for x in item]):
            return f(item, f)
        else:
            result = item.copy()
            for i, x in enumerate(item):
                if type(x) == str: continue
                if all([True if type(y) == str else False for y in x]):
                    result[i] = f(x,f)
                else:
                    result[i] = self.not_simple(x, f)
            
            return self.not_simple(result, f)

    def solve(self) -> tuple((int, int)):
        result1, result2 = 0, 0
        for line in self.input:
            parsed, _ = self.parse_to_list(line, 0)
            result1 += int(self.not_simple(parsed, self.left_to_right))
            result2 += int(self.not_simple(parsed, self.reversed_op_precedence))
        return result1, result2

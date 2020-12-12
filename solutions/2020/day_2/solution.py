# prompt: https://adventofcode.com/2020/day/2

from ...base import BaseSolution, InputTypes
# from typing import Tuple
from collections import Counter

class Solution(BaseSolution):
    year = 2020
    number = 2
    input_type = InputTypes.STRSPLIT

#3-10 g: gggxwxggggkgglklhhgg

    def part_1(self) -> int:
        correctPasswords = 0

        for line in self.input:
            number, char, password = line.split(' ')
            charMin, charMax = number.split('-')
            char = char.split(':')[0]
            countChar = Counter(password)
            if char in countChar.keys():
                charNumber = countChar[char]
            else:
                charNumber = 0 
            
            #print(charMin, charMax, char, charNumber, countChar, password)

            if charNumber >= int(charMin) and charNumber <= int(charMax):
                correctPasswords += 1
        return correctPasswords

    def part_2(self) -> int:
        correctPasswords = 0

        for line in self.input:
            correctPosition = 0
            number, char, password = line.split(' ')
            charMin, charMax = number.split('-')
            charMin = int(charMin)
            charMax = int(charMax)
            char = char.split(':')[0]
            if char in password[charMin-1]:
                correctPosition += 1
            if char in password[charMax-1]:
                correctPosition += 1
            if correctPosition == 1:
                correctPasswords += 1
        return correctPasswords


#   def solve(self) -> Tuple[int, int]:
#       pass

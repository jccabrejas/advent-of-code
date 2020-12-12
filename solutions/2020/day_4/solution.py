# prompt: https://adventofcode.com/2020/day/4

from ...base import BaseSolution, InputTypes
# from typing import Tuple
import re
import string
from collections import defaultdict

    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    # hgt (Height) - a number followed by either cm or in:
    #     If cm, the number must be at least 150 and at most 193.
    #     If in, the number must be at least 59 and at most 76.
    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    # cid (Country ID) - ignored, missing or not.
class test_class:
        def is_length_digits(self, num, length):
            return len(num) == length and num.isdigit()

        def is_four_digits(self, num):
            return self.is_length_digits(num, 4)
        
        def is_nine_digits(self, num):
            return self.is_length_digits(num, 9)
        
        def within_limits(self, num, min_limit, max_limit):
            if num[:2] == '':
                return False
            return int(num) >= min_limit and int(num) <= max_limit
        
        def within_byr_limits(self, num):
            return self.within_limits(num, 1920, 2002)

        def within_iyr_limits(self, num):
            return self.within_limits(num, 2010, 2020)

        def within_eyr_limits(self, num):
            return self.within_limits(num, 2020, 2030)

        def within_cm_limits(self, num):
            return self.within_limits(num[:-2], 150, 193)

        def within_in_limits(self, num):
            return self.within_limits(num[:-2], 59, 76)

        def height_in_cm(self, height):
            return height[:-2].isdigit() and height[-2:] == 'cm'

        def height_in_in(self, height):
            return height[:-2].isdigit() and height[-2:] == 'in'

        def is_hair_color(self, hair_color):
            # a hash followed by exactly six characters 0-9 or a-f. '0123456789abcdef'
            return hair_color[0] == '#' and  all(c in '0123456789abcdef' for c in hair_color[1:])

        def is_eye_color(self, eye_color):
            # exactly one of: amb blu brn gry grn hzl oth
            return eye_color in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

        def is_cid(self, num):
            return True

class Solution(BaseSolution):
    year = 2020
    number = 4
    input_type = InputTypes.STRSPLIT
    separator = '\n\n'

    def part_1(self) -> int:
        number_valid_passports = 0
        
        for line in self.input:
            line = line.replace('\n', ' ')
            pass_proccessed = {}
            valid_keys = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'])
            pass_keys = set()

            for _ in line.split(' '):
                k, v = _.split(':')
                if k not in valid_keys: break
                pass_keys.add(k)

            difference = valid_keys - pass_keys
            print(difference)
            if len(difference) == 0 or len(difference - set(['cid'])) == 0: 
                number_valid_passports += 1

        return number_valid_passports

    def part_2(self) -> int:

        tests = {'byr' : ['is_four_digits', 'within_byr_limits'],
            'iyr' : ['is_four_digits', 'within_iyr_limits'],
            'eyr' : ['is_four_digits', 'within_eyr_limits'],
            'hgt' : ['height_in_cm', 'within_cm_limits', 'height_in_in', 'within_in_limits'],
            'hcl' : ['is_hair_color'],
            'ecl' : ['is_eye_color'],
            'pid' : ['is_nine_digits'],
            'cid' : ['is_cid']}

        number_valid_passports = 0
        
        mytests = test_class()

        for line in self.input:
            line = line.replace('\n', ' ')
            pass_proccessed = {}
            valid_keys = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'])
            pass_keys = set()

            test_results = defaultdict(list)
            for _ in line.split(' '):
                k, v = _.split(':')
                if k not in valid_keys: break
                pass_keys.add(k)

                for test in tests[k]:
                    test_results[k].append(getattr(mytests, test)(v))
            print(test_results)

            difference = valid_keys - pass_keys
            print('Missing items: ', difference)
            if len(difference) == 0 or len(difference - set(['cid'])) == 0: 
                passport_checks = []   
                for k, v in test_results.items():
                    if k == 'hgt':
                        passport_checks.append(all(v[0:2]) or all(v[2:]))
                    else:
                        passport_checks.append(all(v))
                if all(passport_checks):
                    number_valid_passports += 1 
                    print('Good passport')
                
        return number_valid_passports

#   def solve(self) -> Tuple[int, int]:
#       pass

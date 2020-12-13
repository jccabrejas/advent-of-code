# prompt: https://adventofcode.com/2020/day/13

from ...base import BaseSolution, InputTypes
# from typing import Tuple
from collections import defaultdict
import numpy as np
from operator import add

class Solution(BaseSolution):
    year = 2020
    number = 13
    input_type = InputTypes.STRSPLIT

    def part_1(self) -> int:
        target = int(self.input[0])
        buses = sorted([int(n) for n in self.input[1].split(',') if n != 'x'])

        waitingTime = defaultdict(int)

        for bus in buses:
            waitingTime[bus] = bus - target % bus

        minWaitingTime = buses[-1]
        myBus = buses[-1]

        for b,w in waitingTime.items():
            if w < minWaitingTime:
                minWaitingTime = w
                myBus = b

        return myBus, minWaitingTime, myBus*minWaitingTime

    def busesaligned(self, t, buses, offset):
        counter = 0
        for idx, b in buses:
            counter += 1
            if (t - (offset - idx)) % b != 0:
                return False
            elif counter == len(buses):
                return True

    def iterationstoalign(self, b1, b2):
        off_1, i = b1
        off_2, j = b2
        offset = off_2 - off_1
        counter = 1
        if offset > 0:
            while counter < j:
                print(counter*i, counter*i + j - (counter*i) % j )
                if ((counter + 1) * i) % j == offset:
                    return counter
                else:
                    counter += 1
        else:
            while counter < j:
                if (counter * i) % j == - offset:
                    return counter
                else:
                    counter += 1
        
        return counter

    def firstaligned(self, b1, b2):
        off_1, i = b1
        off_2, j = b2

        (off_2 - off_1) // i
        t = 0

        for counter in range(1,j+1):
            t = i * counter
            off = (j*(counter*i)//j + j) % j

            if ((off_2 - off_1) + (counter*i)%j) % j == 0 :
                return t
            # print(counter, t, off)

        return None

    def check(self, s, first, delta):
        for f, d in zip(first[1:], delta[1:]):
            if (s - f) % d != 0:
                return False
            else:
                return True
        return True


    def part_2(self) -> int:
        print(self.input[1])
        buses = [(idx, int(b)) for idx, b in enumerate(self.input[1].split(',')) if b != 'x']
        # buses = list(reversed(sorted(buses, key=lambda x: x[1])))
        # buses = sorted(buses, key=lambda x: x[1])
        print(buses)

        first = []
        delta = []
        for b in buses[1:]:
            first.append(self.firstaligned(buses[0], b))
            delta.append(buses[0][1]*b[1])
        
        print(first)
        print(delta)
        start = list(map(add, first, delta))
        # first.append(first[0])
        # first.pop(0)
        # delta.append(delta[0])
        # delta.pop(0)
        # start.append(start[0])
        # start.pop(0)

        while True:
            # check if all alligned
            # 
            if self.check(start[0], first, delta):
                print(start[0])
                return start[0] 
            else:
                start[0] += delta[0]

#   def solve(self) -> Tuple[int, int]:
#       pass

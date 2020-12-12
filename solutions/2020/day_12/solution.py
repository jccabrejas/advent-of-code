# prompt: https://adventofcode.com/2020/day/12

from ...base import BaseSolution, InputTypes
# from typing import Tuple
from collections import defaultdict
from math import sin, cos, atan2, pi, sqrt

class Solution(BaseSolution):
    year = 2020
    number = 12
    input_type = InputTypes.STRSPLIT

    def part_1(self) -> int:
        navigation = defaultdict(int)
        x, y = 0, 0
        degree = 0
        for line in self.input:
            action, value = line[0], int(line[1:])
            if action == 'N':
                y += value
            elif action == 'S':
                y -= value
            elif action == 'E':
                x += value
            elif action == 'W':
                x -= value
            elif action == 'R':
                degree -= value
            elif action == 'L':
                degree += value
            elif action == 'F':
                x += value * cos(2 * pi * degree / 360.)
                y += value * sin(2 * pi * degree / 360.)

        result = abs(x) + abs(y)
    
        return result
    
    def part_2(self) -> int:
        navigation = defaultdict(int)
        x, y = 0, 0
        dx, dy = 10, 1
        distance = sqrt(dx**2 + dy**2)
        to_radians = 2 * pi / 360.
        to_degrees = 1 / to_radians
        degree = atan2(dy,dx) * to_degrees

        for line in self.input:
            action, value = line[0], int(line[1:])
            print((x,y), (dx,dy), degree, action, value)
            if action == 'N':
                dy += value
                distance = sqrt(dx**2 + dy**2)
                degree = atan2(dy,dx) * to_degrees
            elif action == 'S':
                dy -= value
                distance = sqrt(dx**2 + dy**2)
                degree = atan2(dy,dx) * to_degrees
            elif action == 'E':
                dx += value
                distance = sqrt(dx**2 + dy**2)
                degree = atan2(dy,dx) * to_degrees
            elif action == 'W':
                dx -= value
                distance = sqrt(dx**2 + dy**2)
                degree = atan2(dy,dx) * to_degrees
            elif action == 'R':
                if value == 90:
                    dx, dy = dy, -dx                
                elif value == 180:
                    dx, dy = -dx, -dy
                elif value == 270:
                    dx, dy = -dy, dx

            elif action == 'L':
                if value == 90:
                    dx, dy = -dy, dx
                elif value == 180:
                    dx, dy = -dx, -dy
                elif value == 270:
                    dx, dy = dy, -dx
                degree += value

            elif action == 'F':
                x += value * dx
                y += value * dy

        result = abs(x) + abs(y)
    
        return result
    
#   def solve(self) -> Tuple[int, int]:
#       pass

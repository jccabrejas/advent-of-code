# prompt: https://adventofcode.com/2020/day/11

from ...base import BaseSolution, InputTypes
# from typing import Tuple
import numpy as np

class Solution(BaseSolution):
    year = 2020
    number = 11
    input_type = InputTypes.STRSPLIT

    def adjacents(self, row, col, layout):
        max_row, max_col = layout.shape
        interest = np.s_[max(0,row-1):min(max_row,row+1)+1, 
                        max(0,col-1):min(max_col,col+1)+1]
        layout[row,col] = '_'
        unique, counts = np.unique(layout[interest], return_counts=True)
        
        summary = dict(zip(unique, counts))
        if '#' not in summary.keys():
            return 0
        else:
            return summary['#']

    def check_pos(self, pos, empty, occupied):
        if pos == '.':
            return empty, occupied, False
        elif pos == 'L':
            empty += 1
            return empty, occupied, True
        elif pos == '#':
            occupied += 1
            return empty, occupied, True

    def firstinview(self, row, col, layout):
        max_row, max_col = layout.shape
        empty = 0
        occupied = 0

        # Horizontal check
        for pos in layout[row,col+1:]:
            empty, occupied, flag = self.check_pos(pos, empty, occupied)
            if flag: break

        for pos in np.flip(layout[row,:col]):
            empty, occupied, flag = self.check_pos(pos, empty, occupied)
            if flag: break
        
        # Vertical check
        for pos in layout[row+1:,col]:
            empty, occupied, flag = self.check_pos(pos, empty, occupied)
            if flag: break

        for pos in np.flip(layout[:row,col]):
            empty, occupied, flag = self.check_pos(pos, empty, occupied)
            if flag: break

        #  Top left to bottom right
        offset = col-row
        interest = np.diagonal(layout, offset=offset)
        if offset >= 0:
            fwd = interest[row+1:]
            bwd = np.flip(interest[:row])
        else:
            fwd = interest[col+1:]
            bwd = np.flip(interest[:col])
        
        # print('>v', offset, row, col, interest, fwd, bwd)

        for pos in fwd:
            empty, occupied, flag = self.check_pos(pos, empty, occupied)
            if flag: break
        
        for pos in bwd:
            empty, occupied, flag = self.check_pos(pos, empty, occupied)
            if flag: break

        # bottom left to top right 
        offset = col - (max_row - 1 - row)
        interest = np.flipud(layout).diagonal(offset=offset) 
        if offset >= 0:
            fwd = interest[max_row -1 - row + 1:]
            bwd = np.flip(interest[:max_row -1 - row])
        else:
            fwd = interest[col+1:]
            bwd = np.flip(interest[:col])
        # print('>^',offset, row, col, interest, fwd, bwd)

        for pos in fwd:
            empty, occupied, flag = self.check_pos(pos, empty, occupied)
            if flag: break
        
        for pos in bwd:
            empty, occupied, flag = self.check_pos(pos, empty, occupied)
            if flag: break

        return occupied

    def iterate_layout(self, layout, close=True, limit=4):
        prev = layout.copy()
        rows, cols = layout.shape

        for row in range(rows):
            for col in range(cols):
                seat = prev[row,col]
                if seat == '.':
                    continue

                if close:
                    occupiedAround = self.adjacents(row, col, prev.copy())
                else:
                    occupiedAround = self.firstinview(row, col, prev.copy())

                if seat == 'L' and occupiedAround == 0:
                    layout[row, col] = '#'
                elif seat == '#' and occupiedAround >= limit:
                    layout[row, col] = 'L'
        
        return layout

    def part_1(self):

        layout = np.array([list(row) for row in self.input])
        prev = layout.copy()
        while True:
            # print(prev)
            nextLayout = self.iterate_layout(prev.copy(), close=True)
            if (nextLayout == prev).all():
                break
            prev = nextLayout.copy()

        unique, count = np.unique(nextLayout, return_counts=True)
        summary = dict(zip(unique, count))
        return summary['#']

    def part_2(self) -> int:
        layout = np.array([list(row) for row in self.input])
        mr, mc = layout.shape
        prev = np.array((mr+2)*(mc+2)*['.']).reshape(mr+2,mc+2)
        prev[1:1+mr,1:1+mc] = layout.copy()
        while True:
            # print(prev)
            nextLayout = self.iterate_layout(prev.copy(), close=False, limit=5)
            if (nextLayout == prev).all():
                break
            prev = nextLayout.copy()

        unique, count = np.unique(nextLayout, return_counts=True)
        summary = dict(zip(unique, count))
        return summary['#']

#   def solve(self) -> Tuple[int, int]:
#       pass

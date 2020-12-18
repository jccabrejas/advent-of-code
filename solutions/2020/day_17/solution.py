# prompt: https://adventofcode.com/2020/day/17

from ...base import BaseSolution, InputTypes
# from typing import Tuple
import numpy as np

class Solution(BaseSolution):
    year = 2020
    number = 17
    input_type = InputTypes.STRSPLIT

    # If a cube is active and exactly 2 or 3 of its neighbors are also active, the cube remains active. Otherwise, the cube becomes inactive.
    # If a cube is inactive but exactly 3 of its neighbors are active, the cube becomes active. Otherwise, the cube remains inactive.

    def adjacents(self, x, y, z, f, layout):
        max_x, max_y, max_z, max_f = layout.shape
        interest = np.s_[x-1:x+2, y-1:y+2, z-1:z+2, f-1:f+2]

        unique, counts = np.unique(layout[interest], return_counts=True)
        
        summary = dict(zip(unique, counts))
        if True in summary:
            return summary[True] - layout[x,y,z, f]
        else:
            return 0

    def iterate_layout(self, layout, counter):
        prev = layout.copy()
        rows, cols, depth, timespan = layout.shape

        for f in range(1+counter, timespan-1-counter):
            for z in range(1+counter, depth-1-counter):
                for x in range(1+counter, rows-1-counter):
                    for y in range(1+counter, cols-1-counter):

                        cellAdjacents = self.adjacents(x, y, z, f, prev)
                        if prev[x,y,z,f]:
                            if not (cellAdjacents in [2,3]):
                                layout[x,y,z,f] = False

                        else:
                            if cellAdjacents in [3]:
                                layout[x,y,z,f] = True
        
        return layout

    def part_1(self) -> int:
        # parse input
        # loop through cycle count
        # for each position
        #   active/inactive
        #   number of 3D adjacents
        layout = np.array([[True if x =='#' else False for x in row ] for row in self.input])
        mr, mc = layout.shape
        cycles = 6
        initialSize = 25
        fourth = 25
        prev = np.array((initialSize*mr)*(initialSize*mc)*(initialSize)*fourth*[False]).reshape(initialSize*mr,initialSize*mc,initialSize,fourth)
        
        x0 = (initialSize - 1)//2*mr
        y0 = (initialSize - 1)//2*mc
        z0 = (initialSize - 1)//2
        f0 = (fourth - 1) // 2
        prev[x0:x0+mr,y0:y0+mc,z0, f0] = layout
        print(prev[x0-1:x0+mr+1,y0-1:y0+mc+1,z0, f0])

        counter = 0
        while counter < cycles:
            nextLayout = self.iterate_layout(prev.copy(), counter)
            prev = nextLayout.copy()
            counter += 1
            print(prev[x0-1:x0+mr+1,y0-1:y0+mc+1,z0, f0])

        # Find repeating pattern
        # pattern = np.s_[xr,yr,zr]
        unique, count = np.unique(prev, return_counts=True)
        summary = dict(zip(unique, count))
        return summary[True]

    def part_2(self) -> int:
        pass

#   def solve(self) -> Tuple[int, int]:
#       pass

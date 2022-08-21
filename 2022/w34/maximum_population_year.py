# brute force, TODO: solve in O(n)
from typing import List


class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        start = 1950
        end = 2050
        n = end - start + 1
        alive = [0] * n
        cummax = 0
        i_max = 0
        for birth, death in sorted(logs):
            for y in range(birth, death):
                alive[y - start] += 1
                if alive[y - start] > cummax:
                    cummax = alive[y - start]
                    i_max = y - start
        return i_max + start

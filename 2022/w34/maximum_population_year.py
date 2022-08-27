from typing import List


class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        start = 1950
        end = 2050
        arr = [0] * (end - start + 1)
        for b, d in logs:
            arr[b - start] += 1
            arr[d - start] -= 1
        curmax = 0
        i_max = 0
        cur = 0
        for i, k in enumerate(arr):
            cur += k
            if cur > curmax:
                curmax = cur
                i_max = i
        return i_max + start

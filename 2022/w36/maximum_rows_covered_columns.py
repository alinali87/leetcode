from itertools import combinations
from typing import List


class Solution:
    def maximumRows(self, mat: List[List[int]], cols: int) -> int:
        comb = combinations(range(len(mat[0])), cols)
        nums = [int(''.join(map(str, r)), 2) for r in mat]
        res = 0
        for c in comb:
            s = [0] * len(mat[0])
            for i in c:
                s[i] = 1
            templ = int(''.join(map(str, s)), 2)
            count = 0
            for n in nums:
                if n | templ == templ:
                    count += 1
            res = max(res, count)
        return res

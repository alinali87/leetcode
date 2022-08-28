from cmath import inf
from collections import defaultdict
from typing import List


class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        d = defaultdict(int)
        max_val = -inf
        res = 0
        for i, n in enumerate(edges):
            d[n] += i
            if d[n] > max_val:
                max_val = d[n], max_val
                res = n
            # we need to take the smallest index with the highest score
            elif d[n] == max_val and n <= res:
                res = n
        return res

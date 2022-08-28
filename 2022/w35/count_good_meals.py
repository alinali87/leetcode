from typing import List
from collections import Counter


class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        m = 10 ** 9 + 7
        c = Counter(deliciousness)
        pows = set([2 ** i for i in range(21)])
        seen = set()
        res = 0
        for v, count in c.items():
            for p in pows:
                if v == p and count > 1:
                    res += ((count * (count - 1)) // 2) % m
                if p >= v and p - v in seen:
                    res += (count * c[p - v]) % m

            seen.add(v)
        return res

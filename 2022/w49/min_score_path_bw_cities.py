from collections import defaultdict, deque
from math import inf
from typing import List


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:

        graph = defaultdict(dict)
        for u, v, w in roads:
            graph[u][v] = graph[v][u] = w

        res = inf
        vis = set()
        dq = deque([1])

        while dq:
            node = dq.popleft()
            for adj, scr in graph[node].items():
                if adj not in vis:
                    dq.append(adj)
                    vis.add(adj)
                res = min(res, scr)

        return res

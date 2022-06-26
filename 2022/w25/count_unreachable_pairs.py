from collections import defaultdict
from typing import List


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        global size
        global seen
        def build_adj(edges):
            adj = defaultdict(list)
            for s, e in edges:
                adj[s].append(e)
                adj[e].append(s)
            return adj

        def dfs(v, adj_d):
            global size
            global seen
            seen.add(v)
            size += 1
            for a in adj_d[v]:
                if a not in seen:
                    dfs(a, adj_d)

        def find_comp_size(n, adj_d):
            global size
            global seen
            size = 0
            result = []
            for i in range(n):
                if i not in seen:
                    size = 0
                    dfs(i, adj_d)
                    result.append(size)
            return result

        def compbinations(n):
            return ((n - 1) * n) // 2

        adj_d = build_adj(edges)
        seen = set()
        sizes = find_comp_size(n, adj_d)
        size = 0
        n_pairs = sum(compbinations(size) for size in sizes)
        n_total = compbinations(n)
        return n_total - n_pairs



def test(a, b):
    assert a == b, f'a: {a}, b: {b}'

sol = Solution()
n = 3
edges = [[0,1],[0,2],[1,2]]
o = 0
test(sol.countPairs(n, edges), 0)

n = 7
edges = [[0,2],[0,5],[2,4],[1,6],[5,4]]
o = 14
test(sol.countPairs(n, edges), o)

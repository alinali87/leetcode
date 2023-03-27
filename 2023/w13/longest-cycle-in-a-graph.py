from typing import List


class Solution:
    ans = -1

    def longestCycle(self, edges: List[int]) -> int:
        self.ans = -1
        if len(edges) == 1:
            return self.ans

        def dfs(v: int, dist: dict):
            u = edges[v]
            if u not in seen:  # come to node for the first time
                seen.add(u)
                if u != -1:  # next node exists
                    # it's first time we come to node, distance is not known and cycle at this moment is not possible
                    dist[u] = dist[v] + 1
                    dfs(u, dist)
            elif u in dist:
                self.ans = max(self.ans, dist[v] - dist[u] + 1)

        # for all nodes in edges if not in seen: start dfs
        seen = set()
        for i, v in enumerate(edges):
            if i not in seen:
                seen.add(i)
                # initialize dist with starting node and distance = 0
                dfs(i, {i: 0})
        return self.ans
